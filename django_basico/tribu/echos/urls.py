from django.urls import path

from . import views

app_name = 'echos'  # This is your app name in the URL

urlpatterns = [
    path('', views.echos_list, name='echos-list'),
    path('add/', views.add_echo, name='echos-add'),
    path('<int:id>/', views.echo_detail, name='echo-details'),
    path('<int:id>/edit/', views.edit_echo, name='echo-edit'),
    path('<int:id>/delete/', views.delete_echo, name='echo-delete'),
    path('<int:id>/waves/', views.echo_all_waves, name='echo-waves'),
    path('<int:id>/waves/add/', views.add_wave_to_echo, name='echo-add-wave'),
]
