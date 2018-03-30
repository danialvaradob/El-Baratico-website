from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
from django.template import loader
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

def detail(request, producto_id):
    return HttpResponse("You're looking at question %s." % producto_id)

def results(request, producto_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % producto_id)

def vote(request, producto_id):
    return HttpResponse("You're voting on question %s." % producto_id)
