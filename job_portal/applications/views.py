from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Application
from jobs.models import Job


@login_required
def apply_job(request, job_id):
    print("Apply function called")

    if request.user.role == "recruiter":
        print("Recruiter blocked")
        return redirect("job_list")

    job = Job.objects.get(id=job_id)

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

