from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login

from authentication.forms import LoginForm
# Create your views here.


def auth_login(request):
    form = LoginForm()
    return render(request, 'auth/login.html', {'login_form': form})