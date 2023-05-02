from django.shortcuts import render
#from django.http import HttpResponse
from models import Clientes
from .forms import ClientesFormulario

def todos (request):
    #con esto busco 
    if(request.GET["search"]):
        recuperar_todos=Clientes.objects.filter(nombre_contains=request.GET.get("search",""))
    return render(request,"layouts/clientes/clientes.html", { "recuperar_todos": recuperar_todos}) 
#aca retorna render que es un request es un parametro y va a buscar   layouts una pagina contactos y recupera todo 
#esto va a la base de datos y trae todo lo que haya creado

def ver(request,nombre):
    formulario=Clientes.objects.get(nombre=nombre)
    return render(request, "layouts/clientes/ver-clientes.html",{"formulario":formulario})

def crear(request):
    # va al formulario y busca el formulario para que se haga el formulario de model form
    formulario=ClientesFormulario()
    return render(request,"layouts/clientes/crear-clientes.html",{"formulario":formulario})

def guardar(request):
    if(request.method=="POST"):
        formulario=ClientesFormulario(request.Post)
        if formulario.is_valid():
            formulario.save()

            recuperar_todos=Clientes.objects.all()
        return render(request,"layouts/clientes/clientes.html",{"formulario":formulario,"recuperar_todos":recuperar_todos})
    else:
        return render(request,"layouts/clientes/crear-clientes.html",{"formulario":formulario})

def eliminar( request,nombre):
    if(request.method=="GET"):
        Cliente= Cliente.objects.get(nombre=nombre)
        Cliente.delete()

        recuperar_todos=Clientes.objects.all()
        return render(request,"layouts/clientes/clientes.html", { "recuperar_todos": recuperar_todos}) 
    









