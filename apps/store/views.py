from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Producto,Categoria
from django.views import generic

# Create your views here.


def index(request):
    product_list = Producto.objects.order_by('-id')
    context = {'product_list': product_list}
    return render(request, 'store/index.html', context)
    #return render(request, 'store/image_test.html', context)

''' 
def index(request):
    product_list = Producto.objects.order_by('-id')
    template = loader.get_template('store/index.html')
    context = {
        'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))

'''

def product_list(request,category_slug = None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(stock__gt = 0)
    if category_slug:
        categoria = get_object_or_404(Categoria,slug = category_slug)
        productos = productos.filter(idCategoria = categoria)

    return render(request,'store/index',{'idCategoria':categoria,
                                                            'categorias':categorias,
                                                            'productos':productos})


def product_detail(request,id,slug):
    producto = get_object_or_404(Producto, id = id,slug = slug, stock__gt=0)
    producto_carrito = CartAddProductForm()
    return render(request,
                    'apps/store/producto/detalle',
                    {'producto':producto,
                    'producto_carrito':producto_carrito})



def detail(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'apps/store/detail.html', {'producto': producto})

class DetailView(generic.DetailView):
    model = Producto
    template_name = 'apps/store/detail.html'


def login(request):
    x = 10

def sign_up(request):
    X = 10

def carrito_detalle(request,id,slug):
	x = 0

