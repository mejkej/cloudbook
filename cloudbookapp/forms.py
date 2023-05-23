from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )

    password1 = forms.CharField(
        max_length=20,
        min_length=5,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )

    password2 = forms.CharField(
        max_length=20,
        min_length=5,
        widget=forms.PasswordInput(attrs={'placeholder': 'Comfirm Password'}),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    


class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )