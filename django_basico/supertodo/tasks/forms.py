from django import forms

from .models import Task


class Complete_before(forms.TextInput):
    input_type = 'datetime-local'


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete_before')
        lables = {
            'title': 'Task Title',
            'description': 'Task Description',
            'complete_before': 'Complete Before (days)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'complete_before': Complete_before(attrs={'class': 'form-control mb-3'}),
        }


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete_before', 'done')
        lables = {
            'title': 'Task Title',
            'description': 'Task Description',
            'complete_before': 'Complete Before (days)',
            'done': 'Task Completed',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'complete_before': Complete_before(attrs={'class': 'form-control mb-3'}),
            'done': forms.CheckboxInput(attrs={'class': ' mb-3'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditTaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['readonly'] = True
