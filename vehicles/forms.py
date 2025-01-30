from django import forms
from .models import VehicleRequest
from django.core.exceptions import ValidationError

class VehicleRequestForm(forms.ModelForm):
    class Meta:
        model = VehicleRequest
        fields = ['vehicle', 'start_date', 'end_date', 'purpose']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if end_date and start_date and end_date < start_date:
            raise ValidationError("Data końcowa nie może być wcześniejsza niż początkowa!")
        return cleaned_data