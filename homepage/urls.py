from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('lista', permanent=False)),
    path('lista/', views.lista, name='lista'),
    path('lista/delete/<int:id>', views.delete, name='delete'),
    path('lista/cadastro', views.cadastro, name='cadastro'),
    path('lista/alterar/<int:id>', views.alterar, name='alterar')
]
