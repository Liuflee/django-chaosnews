from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Noticia

def index(request):
    noticias = Noticia.objects.all().order_by('-fecha_subida')
    
    context = {'noticias': noticias}
    return render(request, 'appchaosnews/index.html', context)

def FAQ(request):
    context = {}
    return render(request, 'appchaosnews/FAQ.html', context)

def login(request):
    context = {}
    return render(request, 'appchaosnews/login.html', context)

def quienes_somos(request):
    context = {}
    return render(request, 'appchaosnews/quienes-somos.html', context)

def noticia(request):
    context = {}
    return render(request, 'appchaosnews/noticia.html', context)


