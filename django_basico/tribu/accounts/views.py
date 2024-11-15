# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from shared.forms import LoginForm, RegisterForm
from users.models import Profile


def user_register(request):
    if request.method == 'POST':
        if (form := RegisterForm(request.POST)).is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            user_profile = Profile(
                user=user,
                bio='User bio',
                avatar='default.jpg',
            )

            user_profile.save()

            login(request, user)
            return redirect('echos:echos-list')
    else:
        form = RegisterForm()
    return render(request, 'AuthForms.html', dict(form=form, status='Register'))


def user_login(request):
    if request.method == 'POST':
        if (form := LoginForm(request.POST)).is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if user := authenticate(request, username=username, password=password):
                login(request, user)
                return redirect('echos:echos-list')
    else:
        form = LoginForm()
    return render(request, 'AuthForms.html', dict(form=form, status='Login'))


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
