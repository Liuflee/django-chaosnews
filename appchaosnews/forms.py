from django import forms
from .models import Noticia, Etiqueta, UserProfile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django_ckeditor_5.widgets import CKEditor5Widget
from django.contrib.auth.models import User

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
            "contenido": CKEditor5Widget(config_name="extends"),  
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'en_carrusel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['etiquetas'].queryset = Etiqueta.objects.all()
        self.fields['contenido'].required = False
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Correo electrónico")


class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Nombre')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Apellido')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='')
    email = forms.EmailField(max_length=254, help_text='')
    

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina el campo de contraseña, ya que no queremos que se modifique desde este formulario
        self.fields.pop('password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Validar el nombre de usuario aquí si es necesario
        return username