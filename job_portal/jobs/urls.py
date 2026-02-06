from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path("dashboard/", views.recruiter_dashboard, name="recruiter_dashboard"),
]
