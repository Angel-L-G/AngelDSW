from django import forms

from .models import Task


class Complete_before(forms.TextInput):
    input_type = 'datetime-local'


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        lables = {
            'name': 'Task Title',
            'description': 'Task Description',
            'complete_before': 'Complete Before (days)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'complete_before': Complete_before(attrs={'class': 'form-control mb-3'}),
        }


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before', 'done')
        lables = {
            'name': 'Task name',
            'description': 'Task Description',
            'complete_before': 'Complete Before (days)',
            'done': 'Task Completed',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'complete_before': Complete_before(attrs={'class': 'form-control mb-3'}),
            'done': forms.CheckboxInput(attrs={'class': ' mb-3'}),
        }
