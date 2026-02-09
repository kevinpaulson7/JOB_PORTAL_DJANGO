from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from applications.models import Application
from .models import Job
from .forms import JobForm


# Job listing page
@login_required
def job_list(request):
    jobs = Job.objects.all().order_by("-created_at")

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
    return render(request, "jobs/recruiter_dashboard.html")


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
    }

    return render(request, "jobs/job_detail.html", context)

