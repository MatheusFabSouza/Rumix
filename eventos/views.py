import time
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages
from django.template.loader import render_to_string
from .models import Evento
from .forms import EventoForm

ATRASO_AJAX = 0.5

def eh_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"

def atraso():
    if ATRASO_AJAX:
        time.sleep(ATRASO_AJAX)

@login_required
def pagina_eventos(request):
    return render(request, "rumix/index.html")

@login_required
def tabela_eventos(request):
    atraso()
    eventos = Evento.objects.select_related("fazenda", "animal").order_by("-data")
    return render(request, "eventos/partials/_table.html", {"eventos": eventos})

@login_required
def criar_evento(request):
    if request.method == "POST":
        atraso()
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criado_por = request.user
            evento.save()
            messages.success(request, "Evento criado com sucesso.")
            return JsonResponse({"ok": True})
        return render(request, "eventos/partials/_form.html", {"form": form}, status=400)
    return render(request, "eventos/partials/_form.html", {"form": EventoForm()})

@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        atraso()
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento atualizado com sucesso.")
            return JsonResponse({"ok": True})
        return render(request, "eventos/partials/_form.html", {"form": form, "evento": evento}, status=400)
    return render(request, "eventos/partials/_form.html", {"form": EventoForm(instance=evento), "evento": evento})

@login_required
def excluir_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "GET":
        return render(request, "eventos/partials/_confirm_delete.html", {"evento": evento})
    if request.method == "POST":
        atraso()
        evento.delete()
        messages.success(request, "Evento excluído com sucesso.")
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False}, status=405)

@login_required
def detalhe_evento(request, pk):
    atraso()
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, "eventos/partials/_detail.html", {"evento": evento})

@login_required
def mensagens_ajax(request):
    msgs = get_messages(request)
    html = render_to_string("eventos/partials/_messages.html", {"messages": msgs}, request=request)
    return HttpResponse(html)
