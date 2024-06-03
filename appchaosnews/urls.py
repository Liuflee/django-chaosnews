from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('login/', auth_views.LoginView.as_view(template_name='appchaosnews/login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),
    path('noticia/<int:noticia_id>/editar/', views.editar_noticia, name='editar_noticia'),
    path('noticia/<int:noticia_id>/eliminar/', views.eliminar_noticia, name='eliminar_noticia'),
    path('subir_noticia/', views.subir_noticia, name='subir_noticia'),
    path('buscar/', views.buscar_noticias, name='buscar_noticias'),
]