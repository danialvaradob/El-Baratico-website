from django.db import models
from apps.store.models import Categoria, Producto
from django import forms
import datetime

from django.db import models
from django.utils import timezone


class Categoria(models.Model):
	descripcion = models.CharField(max_length = 100)
	
    def __str__(self):
    	return self.descripcion

class Producto(models.Model):
	nombre = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 250)
	precio = models.IntegerField()
	oferta = models.BooleanField()
	codigo = models.IntegerField()
	idCategoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    def __str__(self):
    	return self.nombre
