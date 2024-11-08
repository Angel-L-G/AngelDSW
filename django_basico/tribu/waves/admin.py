from django.contrib import admin

# Register your models here.
from .models import Wave


@admin.register(Wave)
class WaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'echo', 'user', 'created_at', 'updated_at')
    pass
