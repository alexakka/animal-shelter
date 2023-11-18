from django import forms
from .models import Shelter


class ShelterCreationForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = [
            'shelter_name', 'city', 'address', 'phone', 'email'
        ]

