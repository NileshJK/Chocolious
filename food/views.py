from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

def fun_food(request):
    item_list=Item.objects.all()
    return HttpResponse(item_list)

def item(request):
    return HttpResponse('<h2>This is an Item View</h2>')