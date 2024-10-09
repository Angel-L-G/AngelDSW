from django.urls import path

from . import views

app_name = 'task'  # This is your app name in the URL

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<task_slug>/', views.task_detail, name='task_detail'),
]
