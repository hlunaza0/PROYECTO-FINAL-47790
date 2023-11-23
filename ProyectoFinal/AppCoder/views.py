from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio_view(xx):
    return HttpResponse("Bienvenidos ...!!!!!")

def cursos_view(xx):
    #return HttpResponse("Aqui voy a mostrar los mis cursos")
    return render(xx, "Appcoder/padre.html")