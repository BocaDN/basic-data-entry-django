from django import forms
from .models import Actor

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'role', 'description', 'testimony', 'profile_picture_url']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        testimony = cleaned_data.get('testimony')

        if role in ['victim', 'suspect'] and not testimony:
            raise forms.ValidationError("Testimony is required for victims and suspects.")
        return cleaned_data

