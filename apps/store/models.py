from django.db import models



class Tipo_Usuario(models.Model):
	descripcion = models.CharField(max_length = 100)

class Usuario(models.Model):
	idTipoUsuario = models.ForeignKey(Tipo_Usuario, on_delete = SET_NULL)
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30)
	nombre = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 100)

class Producto(models.Model):
	nombre = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 250)
	precio = models.IntegerField()
	oferta = models.BooleanField(intial = False)
	codigo = models.IntegerField()
	idCategoria = models.ForeignKey(Categoria, on_delete = models.SET_DEFAULT)

class Carrito(models.Model):
	idUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class Carrito_Detalle(models.Model):
	idCarrito = models.ForeignKey(Carrito, on_delete = models.CASCADE)
	idProducto = models.ForeignKey(Producto, on_delete = models.CASCADE)
	cantidad = models.IntegerField()

class Categoria(models.Model):
	descripcion = models.CharField(max_length = 100)


class Historial(models.Model):
	idUsuario = models.ForeignKey(Usuario, on_delete = SET_NULL)
	fecha = models.DateField()


class Historial_Detalle(models.Model):
	idHistorial = models.ForeignKey(Historial, on_delete = SET_NULL)
	idProducto = models.ForeignKey(Producto, on_delete = SET_NULL)
	cantidad = models.IntegerField()