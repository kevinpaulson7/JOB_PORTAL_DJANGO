from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('create/', views.create_job, name='create_job'),
    path("dashboard/", views.recruiter_dashboard, name="recruiter_dashboard"),
    path("<int:job_id>/", views.job_detail, name="job_detail"),
]
