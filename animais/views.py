from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Animal
from .forms import AnimalForm

# -------------------------
# LISTAGEM
# -------------------------
def lista(request):
    animais = Animal.objects.all().order_by('id')  # ordenar evita warning de Paginator
    paginator = Paginator(animais, 10)
    pagina = request.GET.get('p')
    animais_paginados = paginator.get_page(pagina)
    return render(request, 'animais/animais_lista.html', {
        'titulo': 'Animais',
        'object_list': animais_paginados,
        'create_url': 'animais:cadastrar',
        'update_url': 'animais:editar',
        'delete_url': 'animais:excluir',
        'detail_url': 'animais:detalhe',
    })

# -------------------------
# DETALHE
# -------------------------
def detalhe(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animais/animal_detalhe.html', {
        'titulo': animal.nome_animal,
        'descricao': animal.observacao_animal,
        'object': animal,
    })

# -------------------------
# CADASTRO
# -------------------------
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

# -------------------------
# EDIÇÃO
# -------------------------
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

# -------------------------
# EXCLUSÃO
# -------------------------
def excluir(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        messages.success(request, "Animal excluído com sucesso!")
        return redirect('animais:lista')
    return render(request, 'animais/animal_detalhe.html', {
        'titulo': f'Excluir {animal.nome_animal}',
        'descricao': 'Tem certeza que deseja excluir este animal?',
        'object': animal,
        'confirm_delete': True,
    })
