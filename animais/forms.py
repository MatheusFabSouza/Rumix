from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Submit
from crispy_forms.bootstrap import FormActions
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
        widgets = {"observacao_animal": forms.Textarea(attrs={"rows": 4})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "form-card"

        self.helper.layout = Layout(
            HTML("<h2 class='card-title'>Cadastrar Animal</h2>"),

            Div(
                "nome_animal",
                "genero_animal",
                "porte_animal",
                "classificacao_animal",
                "identificacao_animal",
                "observacao_animal",
                "fazenda",
                css_class="text-start"
            ),

            FormActions(
                Submit("submit", "Salvar", css_class="btn-criar"),
                HTML("<a href='/animais/' class='btn btn-outline-success ms-2'>Cancelar</a>")
            )
        )
