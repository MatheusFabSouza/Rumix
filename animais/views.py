from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Animal
from .forms import AnimalForm

def lista(request):
    animais = Animal.objects.all().order_by('id')
    paginator = Paginator(animais, 10)
    pagina = request.GET.get('p')
    animais_paginados = paginator.get_page(pagina)
    return render(request, 'animais/animais_lista.html', {
        'titulo': 'Animais',
        'object_list': animais_paginados,
    })

def detalhe(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animais/animal_detalhe.html', {
        'titulo': animal.nome_animal,
        'animal': animal,  
    })

def cadastrar(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal cadastrado com sucesso!")
            return redirect('animais:lista')
        else:
            messages.error(request, "Verifique os dados e tente novamente.")
    else:
        form = AnimalForm()
    return render(request, 'animais/animal_form.html', {'form': form, 'titulo': 'Novo Animal'})

def editar(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal atualizado com sucesso!")
            return redirect('animais:detalhe', pk=pk)
        else:
            messages.error(request, "Verifique os dados e tente novamente.")
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animais/animal_form.html', {'form': form, 'titulo': 'Editar Animal'})

def excluir(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        messages.success(request, "Animal excluído com sucesso!")
        return redirect('animais:lista')
    return render(request, 'animais/animal_detalhe.html', {
        'titulo': f'Excluir {animal.nome_animal}',
        'animal': animal,        
        'confirm_delete': True,
    })
