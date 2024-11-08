from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required
def user_details(request, username):
    user = get_user_model().objects.get(username=username)
    return render(request, 'users/user_details.html', {'user': user})
