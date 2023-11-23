from django import forms
from .models import Shelter, Animal, Application


class ShelterCreationForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = [
            'shelter_name',
            'city',
            'address',
            'phone',
            'email'
        ]


class AddingAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['animal_name', 'species', 'breed', 'age', 'description', 'image', 'available']
        # fields = [
        #     'animal_name',
        #     'species',
        #     'breed',
        #     'age',
        #     'description',
        #     'image'
        #     ]



class LeaveAnApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'first_name',
            'second_name',
            'phone',
            'email',
        ]
