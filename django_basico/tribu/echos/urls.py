from django.urls import path

from . import views

app_name = 'echos'  # This is your app name in the URL

urlpatterns = [
    path('', views.echosList, name='echos-list'),
    path('add/', views.addEcho, name='echos-add'),
    path('<echoId>/', views.echoDetail, name='echo-details'),
    path('<echoId>/edit/', views.addEcho, name='echos-edit'),
    path('<echoId>/delete/', views.addEcho, name='echos-delete'),
]
