from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def job_list(request):
    return render(request, 'jobs/job_list.html')


@login_required
def recruiter_dashboard(request):
    return render(request, "jobs/recruiter_dashboard.html")

@login_required
def job_list(request):
    return render(request, "jobs/job_list.html")
