from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        
        elif form.is_valid == 'False':
            messages.error(request, 'Not good enough')
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('base')

            else:
                messages.error(request, 'Username or Password Incorrect.')

    else:
        form = CustomAuthenticationForm()
        return render(request, 'signin.html', {'form': form})





def base_view(request):
    if request.method == 'POST':
        return render(request, 'base.html')

    else:
        return render(request, 'base.html')