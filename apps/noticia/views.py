from django.shortcuts import render
from django.views.generic import ListView
from .models import Noticia

# Create your views here.

class NoticiaListView(ListView):
    model = Noticia
    template_name = "noticias/ListadoNoticias.html"
