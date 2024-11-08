from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.


class Echo(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='echos',
    )

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('echos:echo-details', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
