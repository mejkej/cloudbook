from django.shortcuts import render, redirect

# Create your views here.

def base_view(request):
    if request.method == 'POST':
        return render(request, 'base.html')

    else:
        return render(request, 'base.html')

def signin_view(request):
    if request.method == 'POST':
        return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')


def signup_view(request):
    if request.method == 'POST':
        return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')
