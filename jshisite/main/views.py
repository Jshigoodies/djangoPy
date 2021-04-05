from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response):
    return HttpResponse("<h1>Jshi :D</h1>")

def v1(response):
    return HttpResponse("<h1>Hallo!</h1>")

def toDo(reponse, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %ls.id)

def toDo2(response, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text))) # %s is a string or in python str