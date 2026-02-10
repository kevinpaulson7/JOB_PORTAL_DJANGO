from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from .models import Application
from jobs.models import Job
from datetime import date

@login_required
def apply_job(request, job_id):
    today = date.today()

    job = Job.objects.get(id=job_id)

    if job.application_deadline and today > job.application_deadline:
        return redirect("job_detail", job_id=job.id)

    print("Apply function called")

    if request.user.role == "recruiter":
        print("Recruiter blocked")
        return redirect("job_list")


    already_applied = Application.objects.filter(
        user=request.user,
        job=job
    ).exists()

    print("Already applied:", already_applied)

    if not already_applied:
        Application.objects.create(
            user=request.user,
            job=job
        )
        print("Application created")

    return redirect("job_detail", job_id=job.id)

@login_required
def my_applications(request):

    applications = Application.objects.filter(
        user=request.user
    ).order_by("-applied_at")

    return render(
        request,
        "applications/my_applications.html",
        {"applications": applications},
    )