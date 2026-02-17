from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from applications.models import Application
from .models import Job
from .forms import JobForm
from datetime import date


def home(request):
    return render(request, "home.html")

# Job listing page
@login_required
def job_list(request):

    job_type = request.GET.get("type")

    jobs = Job.objects.all().order_by("-created_at")

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    applied_jobs = Application.objects.filter(
        user=request.user
    ).values_list("job_id", flat=True)

    context = {
        "jobs": jobs,
        "applied_jobs": applied_jobs,
    }

    return render(request, "jobs/job_list.html", context)



# Recruiter dashboard
@login_required
def recruiter_dashboard(request):

    if request.user.role != "recruiter":
        return redirect("job_list")

    jobs = Job.objects.filter(recruiter=request.user)

    return render(
        request,
        "jobs/recruiter_dashboard.html",
        {"jobs": jobs},
    )


# Create job
@login_required
def create_job(request):
    if request.user.role != "recruiter":
        return redirect("job_list")

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            return redirect("recruiter_dashboard")
    else:
        form = JobForm()

    return render(request, "jobs/create_job.html", {"form": form})

@login_required
def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)

    applied = Application.objects.filter(
        user=request.user,
        job=job
    ).exists()

    context = {
        "job": job,
        "applied": applied,
        "today": date.today()
    }

    return render(request, "jobs/job_detail.html", context)

@login_required
def view_applicants(request, job_id):

    job = Job.objects.get(id=job_id)

    if request.user != job.recruiter:
        return redirect("job_list")

    applications = Application.objects.filter(job=job)

    # Skill Matching Logic
    for app in applications:

        # Job skills
        job_skills = []
        if job.required_skills:
            job_skills = [
                s.strip().lower()
                for s in job.required_skills.split(",")
            ]

        # User skills
        user_skills = []
        if hasattr(app.user, "userprofile") and app.user.userprofile.skills:
            user_skills = [
                s.strip().lower()
                for s in app.user.userprofile.skills.split(",")
            ]

        # Matching
        matched = set(job_skills).intersection(set(user_skills))

        app.match_percentage = (
            int(len(matched) / len(job_skills) * 100)
            if job_skills else 0
        )

    return render(
        request,
        "jobs/applicants.html",
        {
            "job": job,
            "applications": applications,
        },
    )


@login_required
def update_application_status(request, app_id, status):

    application = Application.objects.get(id=app_id)

    if request.user != application.job.recruiter:
        return redirect("job_list")

    # prevent status change again
    if application.status != "Applied":
        return redirect("view_applicants",
                        job_id=application.job.id)

    application.status = status
    application.save()

    return redirect("view_applicants",
                    job_id=application.job.id)

