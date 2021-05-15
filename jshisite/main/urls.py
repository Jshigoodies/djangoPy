from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # path("", views.index, name="index"),
    # path("v1/", views.v1, name="view 1"),
    path("<int:id>", views.index, name="To Do List"),
    # path("<str:name>", views.toDo2, name="To Do by NAME"),
]
