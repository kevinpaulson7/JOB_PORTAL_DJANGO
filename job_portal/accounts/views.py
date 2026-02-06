from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm
from django.urls import reverse_lazy


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("job_list")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        user = self.request.user

        if user.role == "recruiter":
            return reverse_lazy("recruiter_dashboard")
        else:
            return reverse_lazy("job_list")


class UserLogoutView(LogoutView):
    next_page = "login"
