from django.urls import  path

from app_biblioteca import views





urlpatterns = [
    path('',views.inicio),


    path('libros', views.libro, name="Libro"),
    path('alumno', views.alumno, name="Alumnos"),
    path('profesores', views.profesor, name="Profesores"),
    path('busqueda', views.busqueda, name="Buscador"),

]