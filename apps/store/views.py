from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from .models import Producto,Categoria
from django.views import generic
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.



@login_required
def index(request):
    product_list = Producto.objects.order_by('-id')
    context = {'product_list': product_list}
    return render(request, 'store/index.html', context)
    #return render(request, 'store/image_test.html', context)

 
def home(request):
    return render(request, 'home.html')


def product_list(request,category_slug = None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(stock__gt = 0)
    if category_slug:
        categoria = get_object_or_404(Categoria,slug = category_slug)
        productos = productos.filter(idCategoria = categoria)

    return render(request,'store/index.html',{'idCategoria':categoria,
                                                            'categorias':categorias,
                                                            'productos':productos})


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
            return redirect('/home.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def carrito_detalle(request):
    return render(request, 'shopping_cart.html')



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

