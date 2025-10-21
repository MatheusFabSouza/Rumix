from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages

def inicio(request):
    return render(request, 'rumix/index.html', {'titulo': 'Rumix'})

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect('rumix:login')
        else:
            messages.error(request, "Erro ao criar conta. Verifique os dados.")
    else:
        form = UserCreationForm()

    return render(request, 'rumix/login_cadastro.html', {
        'signup_form': form,
        'mode': 'cadastro'
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('rumix:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, "Login realizado com sucesso!")
            return redirect('rumix:index')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()

    return render(request, 'rumix/login_cadastro.html', {
        'login_form': form,
        'mode': 'login'
    })

def logout_view(request):
    auth_logout(request)
    messages.info(request, "Você saiu da conta.")
    return redirect('rumix:index')

def perfil(request):
    return render(request, 'rumix/perfil.html', {
        'titulo': f'Perfil — {request.user.username if request.user.is_authenticated else "Visitante"}',
        'usuario': request.user,
    })

def sobre(request):
    return render(request, 'rumix/sobre.html', {
        "titulo": "Sobre",
        })
