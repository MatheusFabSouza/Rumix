from django.db import models
from django.contrib.auth.models import User

class Fazenda(models.Model):
    nome_fazenda = models.CharField(max_length=120)
    dono = models.ForeignKey(User, on_delete=models.PROTECT)
    foto_fazenda = models.ImageField(upload_to='fazendas/', blank=True, null=True)
    sobre_fazenda = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_fazenda
