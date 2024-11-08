from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.bio

    def get_absolute_url(self):
        return reverse('users:user-profile', kwargs={'id': self.id})
