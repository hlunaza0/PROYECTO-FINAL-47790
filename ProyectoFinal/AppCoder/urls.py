from django.urls import path
from AppCoder.views import inicio_view, cursos_view

from django.http import HttpResponse

def inicio_view(xx):
    return HttpResponse("Bienvenidos ...!!!!!")

def cursos_view(xx):
    return HttpResponse("Aqui voy a mostrar los mis cursos")

urlpatterns = [
    path('inicio/', inicio_view),
    path("cursos/", cursos_view)
]

