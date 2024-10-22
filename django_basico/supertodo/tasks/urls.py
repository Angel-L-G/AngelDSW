from django.urls import path

from . import views

app_name = 'tasks'  # This is your app name in the URL

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.addTask, name='add-task'),
    path('done/', views.done, name='done'),
    path('pending/', views.pending, name='pending'),
    path('task/<task_slug>/', views.task_detail, name='task-detail'),
    path('task/<task_slug>/toggle/', views.toggle, name='task-toggle'),
    path('task/<task_slug>/edit/', views.edit, name='task-edit'),
    path('task/<task_slug>/delete/', views.delete, name='task-delete'),
]
