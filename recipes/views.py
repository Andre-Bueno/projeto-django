from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'André Luiz'
    })

def contato(request):
    return render(request, 'recipes/contatos.html')

def sobre(request):
    return HttpResponse('Sobre - Pagina Sobre')


