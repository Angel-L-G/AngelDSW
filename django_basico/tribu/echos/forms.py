from django import forms

from .models import Echo


class AddEchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)
        lables = {
            'content': 'Echo content',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }
