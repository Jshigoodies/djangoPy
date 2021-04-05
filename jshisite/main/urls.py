from django.urls import path

from . import views

urlpatterns = [
path("", views.index, name="index"), 
path("v1/", views.v1, name="view 1"),
path("<int:id>", views.toDo, name="To Do by ID"),
path("<str:name>", views.toDo2, name="To Do by NAME"),
]