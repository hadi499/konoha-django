from django import forms

from .models import Shinobi


class ShinobiForm(forms.ModelForm):
    class Meta:
        model = Shinobi
        fields = [
            'name',
            'email',
            'description',
            'image',
        ]
