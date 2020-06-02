from django import forms
from .models import Icalc


class IcalcForm(forms.ModelForm):
    class Meta:
        model = Icalc
        fields = '__all__'
