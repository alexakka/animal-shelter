from django import forms
from .models import Shelter, Application


class ShelterCreationForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = [
            'shelter_name', 'city', 'address', 'phone', 'email'
        ]


class LeaveAnApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'first_name', 'second_name', 'phone', 'email',
        ]
