from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import FormUsuario


def index(request):
    usuario = Usuario.objects.all()
    return render(request, "index.html", {"usuarios":usuario})

def delete(request, id):
	usuario = get_object_or_404(Usuario, pk=id)
	usuario.delete()
	return redirect('/')

def cadastro(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "cadastro.html", {"form":form})
    else:
        form = FormUsuario()
    return render(request, "cadastro.html", {"form":form})