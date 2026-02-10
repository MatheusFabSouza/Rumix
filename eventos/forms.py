from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    data = forms.DateTimeField( #pra questão de data e hora por ser eventos e ordem de ano mes dia hora e minuto
        input_formats=[
            '%Y-%m-%dT%H:%M',        
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M',
        ],
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M'
        )
    )

    class Meta:
        model = Evento
        fields = ['titulo', 'data', 'fazenda', 'animal', 'descricao']
