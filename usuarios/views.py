from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm, UsuarioCreationForm
from .forms import UsuarioUpdateForm

def cadastrar_usuario(request):
    if request.method == "POST":
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect("usuarios:login")
        else:
            messages.error(request, "Erro ao criar conta. Verifique os dados.")
    else:
        form = UsuarioCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required(login_url='usuarios:login')
@permission_required("usuarios.view_usuario", raise_exception=True)
def usuarios(request):
    usuarios = Usuario.objects.all().order_by("id")
    return render(request, "usuarios/tabela_usuarios.html", {
        "usuarios": usuarios,
        "nome_pagina": "Usuarios",
    })

@login_required(login_url='usuarios:login')
@permission_required("usuarios.add_usuario", raise_exception=True)
def usuarios_novo(request):
    if request.method == "POST":
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario criado com sucesso.")
            return redirect("usuarios:usuarios")
        messages.error(request, "Erro ao criar usuario.")
    else:
        form = UsuarioCreationForm()
    return render(request, "usuarios/novo_usuario.html", {
        "form": form,
        "titulo_pagina": "Adicionar novo Usuario",
    })

@login_required(login_url='usuarios:login')
@permission_required("usuarios.view_usuario", raise_exception=True)
def usuarios_detalhar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, "usuarios/detalhar.html", {
        "usuario": usuario,
        "titulo_pagina": "Detalhar usuario",
    })

@login_required(login_url='usuarios:login')
@permission_required("usuarios.change_usuario", raise_exception=True)
def usuarios_editar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario modificado.")
            return redirect("usuarios:usuarios")
        messages.error(request, "Erro ao mexer em usuario.")
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, "usuarios/editar.html", {
        "form": form,
        "usuario": usuario,
        "titulo_pagina": "Editar usuario",
    })

@login_required(login_url='usuarios:login')
@permission_required("usuarios.delete_usuario", raise_exception=True)
def usuarios_remover(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == "POST":
        usuario.delete()
        messages.success(request, "Usuario deletado.")
        return redirect("usuarios:usuarios")
    return render(request, "usuarios/remover.html", {
        "object": usuario,
        "titulo_pagina": "Remover Usuario",
    })

@login_required
def perfil(request):
    return render(request, "usuarios/perfil.html")

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UsuarioUpdateForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect("usuarios:perfil")
    else:
        form = UsuarioUpdateForm(instance=usuario)
    
    return render(request, "usuarios/editar_perfil.html", {
        "titulo": "Editar Perfil",
        "form": form
    })