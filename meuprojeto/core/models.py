from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    avatar_url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.nome}"