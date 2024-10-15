from django.urls import path

from . import views

app_name = 'task'  # This is your app name in the URL

urlpatterns = [
    path('', views.home, name='home'),
    path('task/add/', views.addTask, name='add_task'),
    path('task/done/', views.done, name='done'),
    path('task/undone/', views.undone, name='undone'),
    path('task/<task_slug>/', views.task_detail, name='task_detail'),
]
