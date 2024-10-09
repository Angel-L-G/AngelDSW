from django.urls import path

from . import views

app_name = 'blog'  # This is your app name in the URL

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<post_id>/', views.post_detail, name='post_detail'),
]
