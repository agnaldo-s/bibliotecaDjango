from django.contrib import admin
from .models import Livro, Genero

class LivrosAdmin(admin.ModelAdmin):
    list_display=['nome', 'qtd_paginas','genero'] 
    search_fields = ['nome']

  
admin.site.register(Livro, LivrosAdmin)
admin.site.register(Genero)
