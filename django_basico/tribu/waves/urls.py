from django.urls import path

from . import views

app_name = 'waves'  # This is your app name in the URL

urlpatterns = [
    path('<int:id>/edit/', views.edit_wave, name='wave-edit'),
    path('<int:id>/delete/', views.delete_wave, name='wave-delete'),
]
