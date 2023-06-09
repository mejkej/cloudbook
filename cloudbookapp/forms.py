from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import get_default_password_validators
from .models import Note

# My CustomUserCreationForm
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )

    password1 = forms.CharField(
        min_length=5,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )

    password2 = forms.CharField(
        min_length=5,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
    )

    # Makes sure username is available if not returns that info
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is not available.')
        return username

    
    # Validates password with AUTH_PASSWORD_VALIDATOR from settings.py
    # Then automatically generates error messages incase of error
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password_validators=get_default_password_validators()
        errors=[]
        for validator in password_validators:
            try:
                validator.validate(password1,self.instance)
            except ValidationError as error:
                errors.extend(error.messages)
        if errors:
            raise ValidationError(errors)
        return password1
    

    # Password1 = Password2 els return message 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords dont match')
        return password2


    class Meta:
        model = User
        fields = ("username", "password1", "password2")

# CustomAuthenticationForm
class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
    # Compare input to registered users
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        # Login or return message
        if not username or not password:
            raise forms.ValidationError('Username or password incorrect.')
        return cleaned_data


# My Note model form
class NoteForm(forms.ModelForm):
    title = forms.CharField(
        min_length=1,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': '1 - 50 characters'}),
    )


    class Meta:
        model = Note
        fields = ['title', 'content']