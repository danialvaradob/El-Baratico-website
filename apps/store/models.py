from django.db import models



class Tipo_Usuario(models.Model):
	descripcion = models.CharField(max_length = 100)

class Usuario(models.Model):
	idTipoUsuario = models.ForeignKey(Tipo_Usuario, on_delete = models.CASCADE)
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30)
	nombre = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 100)

class Carrito(models.Model):
	