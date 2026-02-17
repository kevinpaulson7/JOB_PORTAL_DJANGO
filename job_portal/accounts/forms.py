from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import UserProfile

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "role",
            "password1",
            "password2",
        ]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
            }),
            "role": forms.Select(attrs={
                "class": "form-control"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["skills", "resume"]

        widgets = {
            "skills": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Python, Django, SQL"
                }
            ),
        }


