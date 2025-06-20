from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': 'w-full py-2 px-4 rounded-sm'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={  # Changed from password1 to password
        'placeholder': "Your password",
        'class': 'w-full py-2 px-4 rounded-sm'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': 'w-full py-2 px-4 rounded-sm'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Your email",
        'class': 'w-full py-2 px-4 rounded-sm'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Your password",
        'class': 'w-full py-2 px-4 rounded-sm'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Confirm Password",
        'class': 'w-full py-2 px-4 rounded-sm'
    }))