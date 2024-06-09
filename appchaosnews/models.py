from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username + ' Profile'
    

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    contenido = CKEditor5Field('contenido', config_name='extends')  # Cambiado a RichTextField
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
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='comentario_likes', blank=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.noticia.titulo}'
    
