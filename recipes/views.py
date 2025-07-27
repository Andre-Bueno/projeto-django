from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'André Luiz'
    })

def temp(request):
    return render(request, 'apagar/temp.html')

def sobre(request):
    return HttpResponse('Sobre - Pagina Sobre')

def contato(request):
    return HttpResponse('Contato - Pagina de Contato')
