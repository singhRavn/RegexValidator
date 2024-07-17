from django import forms
from .models import Vehicle

class VehicleForms(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["registration_number"]