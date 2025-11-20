from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages

def inicio(request):
    return render(request, 'rumix/index.html', {'titulo': 'Rumix'})

def login_view(request):
    return redirect('usuarios:login')

def cadastro(request):
    return redirect('registration:register')

def logout_view(request):
    auth_logout(request)
    messages.info(request, "Você saiu com sucesso.")
    return redirect('rumix:index')

def perfil(request):
    return render(request, 'rumix/perfil.html', {'titulo': 'Perfil'})

def sobre(request):
    return render(request, 'rumix/sobre.html', {'titulo': 'Sobre'})

