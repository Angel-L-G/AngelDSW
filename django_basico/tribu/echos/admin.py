from django.contrib import admin

from .models import Echo

# Register your models here.


@admin.register(Echo)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'created_at', 'updated_at')
    pass
