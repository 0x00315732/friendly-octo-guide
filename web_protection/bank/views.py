from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

def signin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else: 
            messages.error(request, 'Invalid username or password.')

    return render(request, "signin.html")


def signup(request):
    return render(request, "signup.html")


def signout(request):
    return render(request, "signin.html")


@login_required
def index(request):
    return render(request, "index.html")


@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("signin")
    
    return render(request, "dashboard.html")