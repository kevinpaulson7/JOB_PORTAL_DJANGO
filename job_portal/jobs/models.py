

# Create your models here.
from django.db import models
from django.conf import settings


class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ("fulltime", "Full Time"),
        ("micro", "Local / Micro Job"),
    )

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        default="fulltime"
    )
    
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    description = models.TextField()
    salary = models.CharField(max_length=100, blank=True)

    required_skills = models.TextField(
        blank=True,
        help_text="Comma separated skills (e.g. Python, Django, SQL)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateField(null=True, blank=True)

    



    def __str__(self):
        return self.title
