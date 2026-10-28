from django import forms
from .models import FoodDonation

class FoodDonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        fields = '__all__'
