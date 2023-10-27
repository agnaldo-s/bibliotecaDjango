from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=True)
    qtd_paginas = models.IntegerField(unique=True)
    capa_livro = models.ImageField(blank=False)
    autor_livro = models.CharField(max_length=255)
    sacado = models.CharField(max_length=255)
    qtd_livros = models.CharField(max_length=255)

