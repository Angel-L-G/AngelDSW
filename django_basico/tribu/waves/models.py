from django.conf import settings
from django.db import models

# Create your models here.


class Wave(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    echo = models.ForeignKey(
        'echos.Echo',
        related_name='waves',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_at']
