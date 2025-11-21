from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email']
    
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "is_active", "foto_perfil", "data_nascimento", "groups"]
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "email",
            "foto_perfil",
            "data_nascimento",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        # Campos obrigatórios
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True
        # Foto não fica com form-control
        self.fields["foto_perfil"].widget.attrs['class'] = 'form-control-file'