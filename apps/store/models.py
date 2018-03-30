from django.db import models



class Tipo_Usuario(models.Model):
	descripcion = models.CharField(max_length = 100)

class Usuario(models.Model):
	idTipoUsuario = models.ForeignKey(Tipo_Usuario, on_delete = models.CASCADE)
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 30)
	email = models.EmailField()
	nombre = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 100)


class Categoria(models.Model):
        descripcion = models.CharField(max_length = 100, db_index = True)
		slug = models.SlugField(max_length = 100, db_index = True)

		class Meta:
			ordering =('descripcion',)
			verbose_name = 'categoria'
			verbose_name_plural = 'categorias'

        def __str__(self):
                return self.descripcion

        def get_absolute_url(self):
        	return reverse('store:product_list_by_category',args=[self.slug])

class Producto(models.Model):
	nombre = models.CharField(max_length = 50, db_index = True)
	descripcion = models.CharField(max_length = 250)
	precio = models.DecimalField(max_digits = 10,decimal_places = 2)
	oferta = models.BooleanField()
	codigo = models.IntegerField()
	stock = models.PositiveIntegerField()
	slug = models.SlugField(max_length = 50, db_index = True)
	idCategoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	imagen = models.ImageField(upload_to='products/%Y/%m/%d', blank = True)

	class Meta:
		ordering = ('-nombre')
		index_together = (('id','slug'),)

	def __str__(self):
                return self.nombre

    def get_absolute_url(self):
    	return reverse('store:detalle_producto',args = [self.id,self.slug])

class Carrito(models.Model):
	idUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class Carrito_Detalle(models.Model):
	idCarrito = models.ForeignKey(Carrito, on_delete = models.CASCADE)
	idProducto = models.ForeignKey(Producto, on_delete = models.CASCADE)
	cantidad = models.IntegerField()



class Historial(models.Model):
	idUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	fecha = models.DateField()


class Historial_Detalle(models.Model):
	idHistorial = models.ForeignKey(Historial, on_delete = models.CASCADE)
	idProducto = models.ForeignKey(Producto, on_delete = models.CASCADE)
	cantidad = models.IntegerField()


	'''
models.CASCADE)
Cascade deletes. Django emulates the behavior of the SQL 
constraint ON DELETE CASCADE and also deletes the object containing the ForeignKey.
	'''
