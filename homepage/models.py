from django.db import models

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=150)
    data_nasc = models.DateField('Data de nascimento', auto_now=False , auto_now_add=False)
    foto = models.ImageField('Foto',upload_to='img')
    email  = models.EmailField('Email', max_length=254)

    def __str__(self):
        return self.nome