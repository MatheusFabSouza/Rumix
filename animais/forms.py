from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Submit
from crispy_forms.bootstrap import FormActions
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"
        widgets = {
            "observacao_animal": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"

        # Ativa o mesmo estilo do perfil
        self.helper.form_class = "form-card"

        self.helper.layout = Layout(

            # Título igual ao card do perfil
            HTML("<h2 class='card-title'>Cadastrar Animal</h2>"),

            # Campos
            Div(
                "nome_animal",
                "especie",
                "raca",
                "idade",
                "peso",
                "observacao_animal",
                css_class="text-start"
            ),

            # Botões
            FormActions(
                Submit("submit", "Salvar", css_class="btn-criar"),
                HTML("<a href='/animais/' class='btn btn-outline-success ms-2'>Cancelar</a>")
            )
        )
