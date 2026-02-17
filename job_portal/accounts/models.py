from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('jobseeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='jobseeker'
    )


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    skills = models.TextField(
        blank=True,
        help_text="Comma separated skills (e.g. Python, Django, SQL)"
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)