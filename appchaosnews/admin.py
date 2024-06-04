from django.contrib import admin
from .models import Noticia, Etiqueta, Like, Comentario
# Register your models here.

admin.site.register(Noticia)
admin.site.register(Etiqueta)
admin.site.register(Like)
admin.site.register(Comentario)