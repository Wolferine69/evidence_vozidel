from django import forms
from .models import ServisniUkon, Vehicle


class ServisniUkonForm(forms.ModelForm):
    class Meta:
        model = ServisniUkon
        exclude = ['vozidlo']
        widgets = {
            'datum' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'max-width: 250px;'})
        }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
