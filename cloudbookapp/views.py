from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .forms import NoteForm
from .models import Note
# Create your views here.

# Register View
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesful !')
    
        else:
            messages.error(request, '')
        return render(request, 'signup.html', {'form': form})
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login View
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

# Home view
@login_required
def base_view(request):
    return render(request, 'base.html')

# Logout view
@login_required
def signout_view(request):
    logout(request)
    return redirect('signin')


# adding/editing note view
@login_required
def note_view(request):
    if request.method == 'POST': 
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('browse')
        else:
            messages.error('Title must contain between 1 - 100 charachters')
    else:
        form = NoteForm()
    return render(request, 'note.html', {'form': form})

# Browse note list view
@login_required
def browse_notes(request):
    notes = Note.objects.filter(user=request.user)    
    return render(request, 'browse.html', {'notes': notes})