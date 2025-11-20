from django import forms
from .models import Fazenda

class FazendaForm(forms.ModelForm):
    class Meta:
        model = Fazenda
        fields = ['nome_fazenda', 'foto_fazenda', 'sobre_fazenda']
