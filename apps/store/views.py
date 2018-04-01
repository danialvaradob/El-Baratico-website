from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Producto,Categoria
from django.views import generic
from .forms import SignUpForm
# Create your views here.




'''def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.username = form.cleaned_data.get('username')
            user.profile.nombre = form.cleaned_data.get('nombre')
            user.profile.apellidos = form.cleaned_data.get('apellidos')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})'''


def index(request):
    product_list = Producto.objects.order_by('-id')
    context = {'product_list': product_list}
    return render(request, 'store/index.html', context)
    #return render(request, 'store/image_test.html', context)



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



def detail(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'apps/store/detail.html', {'producto': producto})

class DetailView(generic.DetailView):
    model = Producto
    template_name = 'apps/store/detail.html'


def login(request):
    x = 10

'''def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully created!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'store/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })'''

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user,user_profile = form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('apps/store/index.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def carrito_detalle(request,id,slug):
	x = 0


