from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Template, Context

def inicio_view(xx):
    return HttpResponse("Bienvenidos ...!!!!!")

def cursos_view(xx):
    #return HttpResponse("Aqui voy a mostrar mis cursos")
    nombre    = "Hans" 
    apellido  = "Luna"
    diccionario = {"nombre":nombre, "apellido":apellido} #enviar a contexto
    ruta = r"\1.CAPA\1.TECNOLOGIA\3.DATA_ANALYTICS_IA_DS\9.PYTHON\3.CODERHOUSE\PROYECTO-FINAL-47790\ProyectoFinal-2\AppCoder\templates\AppCoder\padre.html"
    mi_archivo = open(ruta,"r")

    # #django version 1
    plantilla =Template(mi_archivo.read()) #se carga en memoria el docuemnto, template
    contexto = Context(diccionario) #asiganamos al contexto nombre y apellido
    documento = plantilla.render(contexto) #renderizamos la plantilla la documento

    # #return render(xx, "Appcoder/padre.html")
    return HttpResponse(documento)        