from django import forms

from .models import Wave


class WaveForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ('content',)
        labels = {
            'content': 'Wave content',
        }
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }
