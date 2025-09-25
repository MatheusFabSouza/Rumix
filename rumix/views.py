from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages

def inicio(request):
    context = {
        "titulo": "Rumix",
    }
    return render(request, "rumix/index.html", context)

def feed_lista(request):
    posts = [] #mudar quando tiver algo
    return render(request, "rumix/feed_lista.html", {"posts": posts})

def feed_detalhe(request, id):
    post = None #mudar quando tiver algo
    return render(request, "rumix/feed_detalhe.html", {"post": post})

def animais_lista(request):
    animais = []  #mudar quando tiver algo
    return render(request, "rumix/animais_lista.html", {"animais": animais})

def animal_detalhe(request, id):
    animal = None #mudar quando tiver algo
    return render(request, "rumix/animal_detalhe.html", {"animal": animal})

def fazendas_lista(request):
    fazendas = [] #mudar quando tiver algo
    return render(request, "rumix/fazendas_lista.html", {"fazendas": fazendas})

def fazenda_detalhe(request, id):
    fazenda = None #mudar quando tiver algo
    return render(request, "rumix/fazenda_detalhe.html", {"fazenda": fazenda})

def leiloes_lista(request):
    leiloes = [] #mudar quando tiver algo
    return render(request, "rumix/leiloes_lista.html", {"leiloes": leiloes})

def leilao_detalhe(request, id):
    leilao = None #mudar quando tiver algo
    return render(request, "rumix/leilao_detalhe.html", {"leilao": leilao})

def sobre(request):
    context = {
        "titulo": "Sobre:",
        "descricao": "Rumix é uma plataforma para conectar agricultores e interessados no meio rural. Criada por Gabriel Sinedino, João Paulo e Matheus Fabricio.",
    }
    return render(request, "rumix/sobre.html", context)


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect('rumix:login')
    else:
        form = UserCreationForm()
    return render(request, 'rumix/cadastro.html', {'form': form})

@login_required
def perfil(request):
    usuario = request.user
    return render(request, 'rumix/perfil.html', {"usuario": usuario})

def login_cadastro(request):
    cadastro_form = UserCreationForm()
    login_form = AuthenticationForm()

    if request.method == 'POST':
        if "login" in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('rumix:perfil')
            else:
                messages.error(request, "Login invalido, tente noamnete.")
        elif "cadastro" in request.POST:
            cadastro_form = UserCreationForm(request.POST)
            if cadastro_form.is_valid():
                cadastro_form.save()
                messages.success(request, "Conta registrada, por favor, faca login.")
                return redirect('rumix:login_cadastro')
            else:
                messages.error(request, "Erro ao criar conta.")

    return render(request, "rumix/login_cadastro.html", {
        "cadastro_form": cadastro_form,
        "login_form": login_form
    })
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()               # salva o usuario
            auth_login(request, user)        # loga o usuario
            return redirect("rumix:index")
    else:
        form = UserCreationForm()
    return render(request, "rumix/signup.html", {"form": form})

# view de login
def login_view(request):
    # se já está logado vai redireciona
    if request.user.is_authenticated:
        return redirect("rumix:index")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("rumix:index")
    else:
        form = AuthenticationForm()
    return render(request, "rumix/login.html", {"form": form})
