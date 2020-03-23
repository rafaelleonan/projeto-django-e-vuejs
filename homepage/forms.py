from django import forms
from .models import Usuario
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

class FormUsuario(forms.ModelForm):
    nome = forms.CharField(max_length=150, required=True)
    data_nasc = forms.DateField(required=True)
    foto = forms.ImageField(required=False)
    email = forms.EmailField(max_length=254, required=True)
    class Meta:
        model = Usuario
        fields = ('nome', 'data_nasc', 'foto', 'email',)