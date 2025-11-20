from django.conf import settings
from django.db import models

class Fazenda(models.Model):
    nome_fazenda = models.CharField(max_length=100)
    dono_fazenda = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    foto_fazenda = models.ImageField( upload_to="fazendas/media/", blank=True, null=True, verbose_name="Imagem da fazenda")
    sobre_fazenda = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_fazenda

    class Meta:
        verbose_name_plural = "Fazendas"
