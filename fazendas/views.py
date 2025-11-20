from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Fazenda
from .forms import FazendaForm

@login_required(login_url='usuarios:login')
def lista(request):
    fazendas = Fazenda.objects.all().order_by('-id')
    return render(request, 'fazendas/lista.html', {'fazendas': fazendas})

@login_required(login_url='usuarios:login')
def detalhe(request, id):
    fazenda = get_object_or_404(Fazenda, id=id)
    return render(request, 'fazendas/detalhe.html', {'fazenda': fazenda})

@login_required(login_url='usuarios:login')
def criar(request):
    if request.method == 'POST':
        form = FazendaForm(request.POST, request.FILES)
        if form.is_valid():
            fazenda = form.save(commit=False)     
            fazenda.dono_fazenda = request.user  
            fazenda.save()
            messages.success(request, "Fazenda criada.")
            return redirect('fazendas:lista')
        else:
            messages.error(request, "Verifique os dados e tente novamente.")
    else:
        form = FazendaForm()
    return render(request, 'fazendas/form.html', {'form': form, 'titulo':'Nova Fazenda'})

@login_required(login_url='usuarios:login')
def editar(request, id):
    fazenda = get_object_or_404(Fazenda, id=id)
    if request.method == 'POST':
        form = FazendaForm(request.POST, request.FILES, instance=fazenda)
        if form.is_valid():
            form.save()
            messages.success(request, "Fazenda modificada.")
            return redirect('fazendas:detalhe', id=id)
    else:
        form = FazendaForm(instance=fazenda)
    return render(request, 'fazendas/form.html', {'form': form, 'titulo': 'Editar Fazenda'})

@login_required(login_url='usuarios:login')
def excluir(request, id):
    fazenda = get_object_or_404(Fazenda, id=id)
    if request.method == 'POST':
        fazenda.delete()
        messages.success(request, "Fazenda excluída.")
        return redirect('fazendas:lista')
    return render(request, 'fazendas/detalhe.html', {
        'fazenda': fazenda,
        'confirm_delete': True,
        'titulo': f'Excluir {fazenda.nome_fazenda}',
    })
