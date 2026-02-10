from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "company",
            "location",
            "description",
            "salary",
            "application_deadline"
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter job title"
            }),
            "company": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company name"
            }),
            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Job location"
            }),
            "salary": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Salary range"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe the job role..."
            }),
            "application_deadline": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }
