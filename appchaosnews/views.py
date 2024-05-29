from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
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
