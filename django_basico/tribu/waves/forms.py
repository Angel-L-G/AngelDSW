from django import forms

from .models import Wave


class WaveAddForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ('content',)
        labels = {
            'content': 'Wave content',
        }
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }


class WaveEditForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ('content',)
        labels = {
            'content': 'Wave content',
        }
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }
