from django.contrib import admin

# Register your models here.
from .models import Producto,Categoria
'''
class adminCategoria(admin.ModelAdmin):
	list_display = ['descripcion','slug']
	prepopulated_fields = {'slug':('descripcion',)}


class adminProduct(admin.ModelAdmin):
	list_display = ['nombre','slug','idCategoria','precio','stock']
'''
admin.site.register(Producto)
admin.site.register(Categoria)
