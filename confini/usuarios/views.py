from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import*

# Create your views here.
def homepage(request):
    usuarios = Usuario.objects.all()
    contexto = {
        'usuario':usuarios
    }
    return render(request, "inicio/inicio.html", contexto)

class CreateUser(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/nuevoreg.html'
    success_url = reverse_lazy('usuarios:lista')

def listUser(request):
    usuario = Usuario.objects.all()
    contexto = {
        'usuario': usuario
    }
    return render(request, 'usuarios/lista.html', contexto)

class EditUser(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name  = 'usuarios/editar.html'
    success_url = reverse_lazy('usuarios:lista')

def deleteUser(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    return redirect('usuarios:lista')



