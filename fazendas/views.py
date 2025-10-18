from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Fazenda
from .forms import FazendaForm

def lista(request):
    fazendas = Fazenda.objects.all().order_by('-id')
    return render(request, 'fazendas/lista.html', {'fazendas': fazendas})

def detalhe(request, pk):
    fazenda = get_object_or_404(Fazenda, pk=pk)
    return render(request, 'fazendas/detalhe.html', {'fazenda': fazenda})

@login_required
def criar(request):
    if request.method == 'POST':
        form = FazendaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Fazenda criada.")
            return redirect('fazendas:lista')
    else:
        form = FazendaForm()
    return render(request, 'fazendas/form.html', {'form': form, 'titulo':'Nova Fazenda'})

@login_required
def editar(request, pk):
    fazenda = get_object_or_404(Fazenda, pk=pk)
    if request.method == 'POST':
        form = FazendaForm(request.POST, request.FILES, instance=fazenda)
        if form.is_valid():
            form.save()
            messages.success(request, "Fazenda atualizada.")
            return redirect('fazendas:detalhe', pk=pk)
    else:
        form = FazendaForm(instance=fazenda)
    return render(request, 'fazendas/form.html', {'form': form, 'titulo':'Editar Fazenda'})

@login_required
def excluir(request, pk):
    fazenda = get_object_or_404(Fazenda, pk=pk)
    if request.method == 'POST':
        fazenda.delete()
        messages.success(request, "Fazenda excluída.")
        return redirect('fazendas:lista')
    return render(request, 'fazendas/confirmar_exclusao.html', {'object': fazenda})
