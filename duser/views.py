from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import DUserCreationForm


def home(request):
    context = {
        "title": "Qur'an",
    }
    return render(request, "duser/home.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("Gagal mengautentikasikan"))
            return redirect("login")
    else:
        return render(request, "duser/login_user.html")


def logout_user(request):
    logout(request)
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = DUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect("home")
    else:
        form = DUserCreationForm()
        context = {
            "form": form,
        }
        return render(request, "duser/register_user.html", context)
