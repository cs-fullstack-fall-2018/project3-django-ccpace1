from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'expense_app/account_history.html')


def list(request):
    return HttpResponse("This route works")


def login(request):
    return render(request, "expense_app/login.html")


def logout(request):
    return render(request, "expense_app/logout.html")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(request.POST.get("name"), request.POST.get("email"), request.POST.get("password"))
        return redirect('logout')
    else:
        form = RegistrationForm()
        return render(request, 'expense_app/register.html', {'form': form})
