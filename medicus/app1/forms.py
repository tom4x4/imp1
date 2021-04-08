from django import forms
from .models import Bloz

class Wyszukaj(forms.ModelForm):
    class Meta:
        model = Bloz
        fields = ('kod07',)
