from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()  # Cambiado a RichTextField
    imagen = models.ImageField(upload_to='images/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta)
    en_carrusel = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Like(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='likes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('noticia', 'usuario')


class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = RichTextField(config_name='comments')
    fecha = models.DateTimeField(auto_now_add=True)
