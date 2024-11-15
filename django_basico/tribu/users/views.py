from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from echos.models import Echo

from .forms import User_edit_form

# Create your views here.


@login_required
def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'user_list.html', {'users': users})


@login_required
def user_details(request, username):
    user = get_user_model().objects.get(username=username)
    return render(
        request,
        'user_details.html',
        {
            'other_user': user,
            'echos': Echo.objects.filter(user=user)[:5],
        },
    )


@login_required
def user_echo_details(request, username):
    user = get_user_model().objects.get(username=username)

    return render(
        request,
        'user_details.html',
        {
            'other_user': user,
            'echos': Echo.objects.filter(user=user),
        },
    )


@login_required
def self_profile(request):
    return redirect('users:user-profile', request.user.username)


@login_required
def edit_user(request, username):
    user = get_user_model().objects.get(username=username)
    profile = user.profile

    if request.user != user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        user_form = User_edit_form(request.POST, request.FILES, instance=profile)

        if user_form.is_valid():
            profile = user_form.save()
            return redirect('users:user-profile', username=user.username)
    else:
        user_form = User_edit_form(instance=profile)

    return render(request, 'user_edit_form.html', {'form': user_form})
