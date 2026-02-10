from django.db import models
from django.conf import settings
from jobs.models import Job


class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    job = models.ForeignKey(Job,
                            on_delete=models.CASCADE)

    applied_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20,
                               default="Applied")

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
