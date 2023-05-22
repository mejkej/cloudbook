from django.shortcuts import render, redirect

# Create your views here.

def base_view(request):
    if request.method == 'POST':
        return render(request, 'base.html')

    else:
        return render(request, 'base.html')
