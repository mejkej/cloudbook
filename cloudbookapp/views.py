from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welcome! Lets Sign in.')
            return redirect('signin')
    
        else:
            messages.error(request, '')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome back!')
                return redirect('base')
        else:
            messages.error(request, 'Sign In Error.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'signin.html', {'form': form})


@login_required
def base_view(request):
    return render(request, 'base.html')

@login_required
def signout_view(request):
    logout(request)
    return redirect('signin')