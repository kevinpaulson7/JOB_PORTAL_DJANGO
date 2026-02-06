from django.shortcuts import render

# Create your views here.

def job_list(request):
    return render(request, 'jobs/job_list.html')
