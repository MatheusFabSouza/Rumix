from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'nome_animal',
            'genero_animal',
            'porte_animal',
            'classificacao_animal',
            'identificacao_animal',
            'foto_animal',
            'vacinas_animal',
            'observacao_animal',
            'fazenda'
        ]
        widgets = {
            "observacao_animal": forms.Textarea(attrs={"rows": 4})
        }
