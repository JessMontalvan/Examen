from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import*

# Vista para los tickets
def homepage(request):
     user = User.objects.all()
     contexto = {
        'ticket':user
     }
     return render(request, "inicio/inicio.html", contexto)

class CreateUser(CreateView):
     model = User
     form_class = UserForm
     template_name = 'ticket/nuevotick.html'
     success_url = reverse_lazy('ticket:user')

def listUser(request):
     user = User.objects.all()
     contexto = {
        'usuario': user
     }
     return render(request, 'ticket/user.html', contexto)

class EditUser(UpdateView):
     model = User
     form_class = UserForm
     template_name  = 'ticket/editar.html'
     success_url = reverse_lazy('ticket:user')

def deleteUser(request, id):
     user = User.objects.get(id = id)
     user.delete()
     return redirect('ticket: user')