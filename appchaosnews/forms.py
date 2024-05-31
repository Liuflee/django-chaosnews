from django import forms
from .models import Noticia
from django.contrib.auth.forms import AuthenticationForm

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen', 'etiquetas']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Correo electrónico")