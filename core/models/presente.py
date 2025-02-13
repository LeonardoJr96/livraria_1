from django.db import models
from django.contrib.auth.models import User

class Presente(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="presentes")

    def __str__(self):
        return f"{self.nome} para {self.usuario.username}"
