from django import forms
from .models import Fazenda

class FazendaForm(forms.ModelForm):
    class Meta:
        model = Fazenda
        fields = '__all__'
        widgets = {'sobre_fazenda': forms.Textarea(attrs={'rows':3})}
