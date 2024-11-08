from django.urls import path

from . import views

app_name = 'users'  # This is your app name in the URL

urlpatterns = [
    path('', views.user_list, name='user-list'),
    # path('<str:username>/', views.editWave, name='user-profile'),
    # path('<str:username>/echos/', views.editWave, name='user-echos'),
    # path('<str:username>/edit/', views.editWave, name='wave-edit'),
]
