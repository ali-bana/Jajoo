from django import forms
from .models import House


class HouseRegisterForm(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            'name',
        'owner',
        'rooms',
        'beds',
        'area',
        'max_cap',
        'price_per_night',
        'available',
        'base_image',
        'living_room',
        'bed_room',
        'kitchen',
        'garage',
        'outside',
        ]

class HouseEditForm(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            'name',
            'owner',
            'rooms',
            'beds',
            'area',
            'max_cap',
            'price_per_night',
            'available',
            'base_image',
            'living_room',
            'bed_room',
            'kitchen',
            'garage',
            'outside',
        ]