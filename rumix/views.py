
from django.shortcuts import render, get_object_or_404, redirect

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

def perfil(request):
    usuario = request.user if request.user.is_authenticated else None
    return render(request, "rumix/perfil.html", {"usuario": usuario})

def sobre(request):
    context = {
        "titulo": "Sobre:",
        "descricao": "Rumix é uma plataforma para conectar agricultores e interessados no meio rural. Criada por Gabriel Sinedino, João Paulo e Matheus Fabricio.",
    }
    return render(request, "rumix/sobre.html", context)
