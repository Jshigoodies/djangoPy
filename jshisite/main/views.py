from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

from .forms import CreateNewList

# Create your views here.

# def index(response):
#     return HttpResponse("<h1>Jshi :D</h1>")

# def v1(response):
#     return HttpResponse("<h1>Hallo!</h1>")
#
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})
#
# def toDo2(response, name):
#     ls = ToDoList.objects.get(name=name)
#     item = ls.item_set.get(id=1)
#     return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text))) # %s is a string or in python str

def home(response):
    return render(response, "main/home.html", {})


def create(response):
    form = CreateNewList()
    return render(response, "main/create.html", {"form":form})
