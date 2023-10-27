from django.shortcuts import render,HttpResponse
from biblioteca.models import Livro

def index(request):
    livros = Livro.objects.all()
    return render(request, 'pages/index.html', {'livros':livros})
