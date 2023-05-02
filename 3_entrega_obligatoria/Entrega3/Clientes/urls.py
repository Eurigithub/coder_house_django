from django.urls import path
from django.shortcuts import render
from .import views

urlpatterns=[
    path("",views.todos,name="todos-clientes"),
    path("crear/",views.crear,name="crear-clientes"),
    path("actualizar/<str:nombre>",views.actualizar,name="actualizar-clientes"),
    path("eliminar/<str:nombre",views.eliminar,name="eliminar-clientes"),
    path("ver/<str:nombre>",views.ver,name="ver-clientes"),
    path("guardar/",views.guardar, name="guardar-clientes")
]