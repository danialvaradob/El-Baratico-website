from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from .models import Producto,Categoria, Carrito, Carrito_Detalle, Historial, Historial_Detalle
from django.views import generic
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_protect
import datetime
# Create your views here.



@login_required
def index(request):
    product_list = Producto.objects.order_by('-id')
    historial_list = Historial.objects.filter(idUsuario = request.user)
    context = {'product_list': product_list, 'historial_list': historial_list}
    return render(request, 'store/index.html', context)
    #return render(request, 'store/image_test.html', context)

 
def home(request):
    return render(request, 'home.html')


def product_list(request,category_slug = None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(stock__gt = 0)
    histo = Historial.objects.filter(idUsuario = request.user)
    fechas = []
    historial = []
    for i in histo:
        fechas += [i]
        historial += Historial_Detalle.objects.filter(idHistorial = i)
    if category_slug:
        categoria = get_object_or_404(Categoria,slug = category_slug)
        productos = productos.filter(idCategoria = categoria)

    return render(request,'store/index.html',{'idCategoria':categoria,
                                                            'categorias':categorias,
                                                            'productos':productos,
                                              'historial': historial, 'fechas': fechas})


def product_detail(request,id,slug):
    producto = get_object_or_404(Producto, id = id,slug = slug, stock__gt=0)
    
    return render(request,
                    'apps/store/producto/detail.html',
                    {'producto':producto})


def shopping_cart_list(request):
    userID = request.user.id
    shopping_cart = get_object_or_404(Carrito,idUsuario = userID)
    cart_details = Carrito_Detalle.objects.filter(idCarrito = shopping_cart.id)
    productos = []
    for detail in cart_details:
        productos += get_object_or_404(Producto,id = detail.idProducto)
    return render(request,'apps/store/shopping_cart.html',{'productos':productos})


'''def shopping_cart_list(request):
    userID = request.user.id
    shopping_cart = get_object_or_404(Carrito,idUsuario = userID)
    cart_details = Carrito_Detalle.objects.filter(idCarrito = shopping_cart.id)
    productos = get_object_or_404(Producto,id = cart_details.idProducto)
    return render(request,'apps/store/shopping_cart.html',{'productos':productos})
'''


def detail(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'store/detail.html', {'producto': producto})

class DetailView(generic.DetailView):
    model = Producto
    template_name = 'apps/store/detail.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            c = Carrito(idUsuario=user)
            c.save()
            return redirect('/home.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

'''
def carrito_detalle(request):

    productos = Producto.objects.filter(stock__gt = 0)

    return render(request, 'shopping_cart.html', {'productos': productos})
'''
def carrito_detalle(request):
    userID = request.user.id

    shopping_cart = get_object_or_404(Carrito,idUsuario = userID)
    cart_details = Carrito_Detalle.objects.filter(idCarrito = shopping_cart.id)
    productos = []
    for detail in cart_details:
        productos += [get_object_or_404(Producto,id = detail.idProducto.id)]
    return render(request, 'shopping_cart.html', {'productos': productos})


def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.stock = producto.stock - 1
    producto.save()

    userID = request.user.id
    shopping_cart = get_object_or_404(Carrito,idUsuario = userID)
    cd = Carrito_Detalle(idCarrito=shopping_cart, idProducto=producto, cantidad=1)
    cd.save()
    return redirect('/home.html')

def delete_cart_item(request,producto_id):
    userID= request.user.id
    
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.stock = producto.stock + 1
    producto.save()
    
    shopping_cart = get_object_or_404(Carrito,idUsuario = userID)
    detail = Carrito_Detalle.objects.filter(idCarrito = shopping_cart.id , idProducto = producto_id)
    #detail =get_object_or_404(Carrito_Detalle, idCarrito = shopping_cart.id , idProducto = producto_id)
    for item in detail:
        if item:
            item.delete()
    return redirect('/home.html')

def delete_all_cart_items(request):
    userID= request.user.id
    shopping_cart = get_object_or_404(Carrito,idUsuario = userID)
    h = Historial(idUsuario=request.user, fecha=datetime.date.today())
    h.save()
    
    detail = Carrito_Detalle.objects.all()
    for item in detail:
        if item:
            hd = Historial_Detalle(idHistorial=h, idProducto=item.idProducto, cantidad=1)
            hd.save()
            item.delete()
    return redirect('/home.html')

'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Simple is Better Than Complex{% endblock %}</title>
  </head>
  <body>
    <header>
      <h1>My Site</h1>
      {% if user.is_authenticated %}
        <a href="{% url 'logout' %}">logout</a>
      {% else %}
        <a href="{% url 'login' %}">login</a> / <a href="{% url 'signup' %}">signup</a>
      {% endif %}
      <hr>
    </header>
    <main>
      {% block content %}
      {% endblock %}
    </main>
  </body>
</html>
 usar el if user.is_authenticated y cosas asi. 
'''

