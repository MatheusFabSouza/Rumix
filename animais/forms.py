from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        widgets = {
            'observacao_animal': forms.Textarea(attrs={'rows':3}),
        }
