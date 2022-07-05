from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('titulo', max_length=40, blank = False, null = False )
    subtitulo = models.CharField(max_length=40)
    cuerpo = RichTextField()
    autor = models.CharField(max_length=40)
    fecha = models.DateField(default=datetime.now)
    imagen = models.URLField(max_length = 255, blank = False, null= False)
    estado = models.BooleanField('Publicado/No publicado', default = True) 

    class Meta:
        verbose_name_plural = "Posts"
        verbose_name = "Post"

    def __str__(self):
        return self.titulo

class Autores(models.Model):
    nombre = models.CharField(max_length=40)  
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    imagen = models.URLField(max_length = 255, blank = False, null= False)
    
    class Meta:
        verbose_name_plural = "Autores"
        verbose_name = "Autor"

    def __str__(self): 
        return f"{self.nombre}  {self.apellido} - {self.email}"  



class Perfil(models.Model):
    nombre = models.CharField(max_length=40)  
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    
    class Meta:
        verbose_name_plural = "Perfiles"
        verbose_name = "Perfil"

    def __str__(self): 
        return f"{self.nombre}  {self.apellido} - {self.email}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #SUBCARPETA Avatares de media
    imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)