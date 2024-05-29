#from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('login', views.login, name='login'),
    path('quienes-somos', views.quienes_somos, name='quienes-somos'),
    path('noticia', views.noticia, name='noticia')
] 