#from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home - Pagina Inicial')

def sobre(request):
    return HttpResponse('Sobre - Pagina Sobre')

def contato(request):
    return HttpResponse('Contato - Pagina de Contato')
