from django import forms
from .models import Noticia, Etiqueta
from django.contrib.auth.forms import AuthenticationForm
from ckeditor.widgets import CKEditorWidget

class NoticiaForm(forms.ModelForm):
    etiquetas = forms.ModelMultipleChoiceField(
        queryset=Etiqueta.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen', 'etiquetas', 'en_carrusel']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la noticia'}),
            'contenido': CKEditorWidget(),  
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'en_carrusel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['etiquetas'].queryset = Etiqueta.objects.all()
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Correo electrónico")