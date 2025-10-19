from django.db import models
from django.utils import timezone

class Animal(models.Model):
    nome_animal = models.CharField(max_length=100)
    class Genero(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'W', 'Feminino'
    genero_animal = models.CharField(max_length=1, choices=Genero.choices)
    class Porte(models.TextChoices):
        GRANDE = 'G', 'Grande Porte'
        PEQUENO = 'P', 'Pequeno Porte'
    porte_animal = models.CharField(max_length=1, choices=Porte.choices, default=Porte.PEQUENO)
    class Classificacao(models.TextChoices):
        BOVINO = 'B', 'Bovino'
        SUINO = 'S', 'Suíno'
        CAPRINO = 'C', 'Caprino'
        OVINO = 'O', 'Ovino'
        EQUINO = 'E', 'Equino'
        OUTRO = 'X', 'Outro'
    classificacao_animal = models.CharField(max_length=1, choices=Classificacao.choices, default=Classificacao.OUTRO)
    identificacao_animal = models.CharField(max_length=50, blank=True)
    foto_animal = models.ImageField(upload_to='animais/', blank=True, null=True)
    vacinas_animal = models.ImageField(upload_to='animais/vacinas/', blank=True, null=True)
    observacao_animal = models.TextField(blank=True)
    criado_em = models.DateTimeField(default=timezone.now)
    modificado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_animal
