from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
            return redirect('signin')
 
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
                return redirect('base')
            
    else:
        form = CustomAuthenticationForm()
        return render(request, 'signin.html', {'form': form})


def base_view(request):
    if request.method == 'POST':
        return render(request, 'base.html')

    else:
        return render(request, 'base.html')