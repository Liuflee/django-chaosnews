from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('login', views.login, name='login'),
    path('quienes_somos', views.quienes_somos, name='quienes_somos'),
    path('noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),  # Agrega esta línea para el detalle de la noticia
]
