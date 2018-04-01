from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)


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
        stock = models.PositiveIntegerField(default=0)
        slug = models.SlugField(max_length = 50, db_index = True)
        idCategoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
        imagen = models.ImageField(upload_to='products/%Y/%m/%d', blank = True)
        
        class Meta:
                ordering = ('-nombre',)
                index_together = (('id','slug'),)

        def __str__(self):
                return self.nombre

        def get_absolute_url(self):
                return reverse('store:product_detail',args = [self.id,self.slug])

class Carrito(models.Model):
        idUsuario = models.ForeignKey(UserProfile, on_delete = models.CASCADE)

class Carrito_Detalle(models.Model):
        idCarrito = models.ForeignKey(Carrito, on_delete = models.CASCADE)
        idProducto = models.ForeignKey(Producto, on_delete = models.CASCADE)
        cantidad = models.IntegerField()



class Historial(models.Model):
        idUsuario = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
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
