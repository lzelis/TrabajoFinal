from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, TemplateView
from AppCoder.forms import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import *

# Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def inicio(request):
    posts = Posts.objects.all
    return render(request, 'AppCoder/inicio.html', {"posts": posts}) 


def posts(request):
    return render(request, 'AppCoder/posts.html', {"posts": posts})


def autores(request):
    return render(request, 'AppCoder/autores.html', {"autores": autores})

def nosotros(request):

    return render(request, 'AppCoder/nosotros.html')


#Acá viene el LOGIN Y REGISTRO    

def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      # Autenticación de usuario
      user = authenticate(username=username, password=password) # Si este usuario existe me lo trae
      if user is not None:
        login(request,user) # Si existe, lo loguea
        return render(request, 'AppCoder/inicio.html', {'mensaje': f'Bienvenido {username}'})
      else:
        return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, datos incorrectos'})
    else:
      return render(request,'AppCoder/inicio.html', {'mensaje': 'Error, formulario erróneo'})
  
  form = AuthenticationForm() # Creo un formulario vacío si vengo por GET
  return render(request, 'AppCoder/login.html', {'form':form})

def registro(request):

  if request.method == 'POST': # Si es POST, entonces es un formulario que viene lleno

    form = UserCreationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      return render(request, 'AppCoder/inicio.html', {'mensaje': f'Usuario {username} creado correctamente'})
    else:
      return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario'})

  else:
    form = UserCreationForm()
    return render(request, 'AppCoder/registro.html', {'form': form})


@login_required()
def editarPerfil(request):
  username = request.user

  if request.method == 'POST':
    formulario = UserEditForm(request.POST, instance=username)
    if formulario.is_valid():
      informacion = formulario.cleaned_data
      username.email = informacion['email']
      username.password1 = informacion['password1']
      username.password2 = informacion['password2']
      username.save()

      return render(request, 'AppCoder/inicio.html', {'usuario': username, 'mensaje': 'Datos actualizados correctamente'})
  else:
    formulario = UserEditForm(instance=username)
  return render(request, 'AppCoder/editarPerfil.html', {'formulario': formulario, 'usuario': username.username})

def perfil(request):
    return render(request, 'AppCoder/perfil.html')    

def perfil_detail(request):
    return render(request, 'AppCoder/perfil_detail.html')



  #CRUD
  
class PostsList(ListView):

    model = Posts
    template_name = 'AppCoder/posts_list.html'
    

class PostDetail(DetailView):

    model = Posts
    template_name = 'AppCoder/posts_detail.html'


class PostCreate(LoginRequiredMixin, CreateView):

    model = Posts
    success_url = reverse_lazy('posts_list')  # Redirecciono a la vista de posts luego de crear un post
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']


class PostUpdate(LoginRequiredMixin, UpdateView):

    model = Posts
    success_url = reverse_lazy('posts_list')
    fields = ['titulo', 'subtitulo', 'cuerpo']

  
class PostDelete(LoginRequiredMixin, DeleteView):

    model = Posts
    success_url = reverse_lazy('posts_list')
   
       
class AutoresList(ListView):

    model = Autores
    template_name = 'AppCoder/autores_list.html'

class AutoresDetail(DetailView):

    model = Autores
    template_name = 'AppCoder/autores_detail.html'

class AutoresCreate(LoginRequiredMixin, CreateView):

    model = Autores
    success_url = reverse_lazy('autores_list') # Redirecciono a la vista de autores luego de crear un autor
    
    fields = ['nombre', 'apellido', 'email', 'imagen']

class AutoresUpdate(LoginRequiredMixin, UpdateView):

    model = Autores
    success_url = reverse_lazy('autores_list')
    fields = ['nombre', 'apellido', 'email']

class AutoresDelete(LoginRequiredMixin, DeleteView):

    model = Autores
    success_url = reverse_lazy('autores_list')  

