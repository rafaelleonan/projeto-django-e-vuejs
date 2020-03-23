from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista, name='lista'),
    path('lista/delete/<int:id>', views.delete, name='delete'),
    path('lista/cadastro', views.cadastro, name='cadastro'),
    path('lista/alterar/<int:id>', views.alterar, name='alterar')
]
