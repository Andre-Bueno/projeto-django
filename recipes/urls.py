from django.urls import path
from recipes.views import home, sobre, contato, temp

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('temp/', temp),
]