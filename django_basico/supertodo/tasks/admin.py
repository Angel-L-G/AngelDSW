from django.contrib import admin

from .models import Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'description', 'done', 'complete_before', 'created_at', 'updated_at')
    pass