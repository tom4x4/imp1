from django import forms
from .models import Bloz

class BlozForm(forms.ModelForm):
    class Meta:
        models = Bloz
        fields = ('nazwa','kod07')
