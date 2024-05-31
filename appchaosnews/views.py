from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .models import Noticia
from random import sample
from .forms import NoticiaForm

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
    return render(request, 'appchaosnews/quienes_somos.html', context)

def noticia(request):
    context = {}
    return render(request, 'appchaosnews/noticia.html', context)


def detalle_noticia(request, noticia_id):
    # Obtener la noticia actual
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    
    # Obtener las etiquetas de la noticia actual
    etiquetas = noticia.etiquetas.all()
    
    # Obtener todas las noticias relacionadas que tengan al menos una etiqueta en común
    noticias_relacionadas = Noticia.objects.filter(etiquetas__in=etiquetas).exclude(id=noticia_id).distinct()
    
    # Si hay más de tres noticias relacionadas, seleccionar tres aleatorias
    if noticias_relacionadas.count() > 3:
        noticias_relacionadas = sample(list(noticias_relacionadas), 3)
    
    # Pasar las noticias relacionadas al contexto
    context = {
        'noticia': noticia,
        'noticias_relacionadas': noticias_relacionadas
    }
    
    return render(request, 'appchaosnews/detalle_noticia.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def subir_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect('index')
    else:
        form = NoticiaForm()
    return render(request, 'appchaosnews/subir_noticia.html', {'form': form})