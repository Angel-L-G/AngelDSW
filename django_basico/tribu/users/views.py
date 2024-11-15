from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from echos.models import Echo

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
