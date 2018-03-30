from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, producto_id):
    return HttpResponse("You're looking at question %s." % producto_id)

def results(request, producto_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % producto_id)

def vote(request, producto_id):
    return HttpResponse("You're voting on question %s." % producto_id)