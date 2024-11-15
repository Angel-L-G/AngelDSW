from django import forms

from .models import Profile


class User_edit_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar')
        labels = {
            'bio': 'Bio',
            'avatar': 'Avatar',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control mb-3'}),
        }
