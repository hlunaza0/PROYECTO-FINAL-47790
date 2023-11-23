from django.urls import path
from AppCoder.views import inicio_view, cursos_view

urlpatterns = [
    path("inicio/", inicio_view),
    path("cursos/", cursos_view)
]

