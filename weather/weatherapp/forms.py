from django import forms
from .models import City

class CityForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City Name'}), required=True)

    class Meta:
        model = City
        fields = ["name"]

