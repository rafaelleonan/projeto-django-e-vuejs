from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import FormUsuario


def lista(request):
    usuario = Usuario.objects.all()
    return render(request, "index.html", {"usuarios":usuario})

def delete(request, id):
	usuario = get_object_or_404(Usuario, pk=id)
	usuario.delete()
	return redirect('/')

def cadastro(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data.get("foto"))
            form.save()
            return redirect('/')
        else:
            return render(request, "cadastro.html", {"form":form})
    else:
        form = FormUsuario()
    return render(request, "cadastro.html", {"form":form})

def alterar(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    return render(request, "alterar.html", {"usuario":usuario})