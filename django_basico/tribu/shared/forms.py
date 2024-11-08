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
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        lables = {
            'username': 'username',
            'password': 'password',
            'email': 'email',
            'first_name': 'name',
            'last_name': 'surname',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }
