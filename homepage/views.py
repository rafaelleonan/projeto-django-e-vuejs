from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario


def index(request):
    usuario = Usuario.objects.all()
    return render(request, "index.html", {"usuarios":usuario})

def delete(request, id):
	usuario = get_object_or_404(Usuario, pk=id)
	usuario.delete()
	return redirect('/')