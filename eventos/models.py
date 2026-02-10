from django.db import models
from django.conf import settings
from django.utils import timezone
from fazendas.models import Fazenda
from animais.models import Animal

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data = models.DateTimeField(default=timezone.now) 
    fazenda = models.ForeignKey(Fazenda, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos')
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos')
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} — {self.data:%d-%m-%Y %H:%M}"