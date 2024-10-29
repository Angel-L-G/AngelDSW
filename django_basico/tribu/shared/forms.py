from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
    )
    password = forms.CharField(
        max_length=64,
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
    )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        lables = {
            'username': 'username',
            'email': 'email',
            'password': 'username',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
        }
