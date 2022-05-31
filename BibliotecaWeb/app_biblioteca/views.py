from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from app_biblioteca.models import Libro, Alumno, Profesor
# Create your views here.

def inicio(request):
    return render(request,'app_biblioteca/inicio.html')


def libro(request):
    if request.method == 'POST':
        libro = Libro(titulo=request.POST['titulo'], autor=request.POST['autor'],
                       años_publicacion=request.POST['años_publicacion'],
                       numeros_ejemplares=request.POST['numeros_ejemplares']
                       )

        libro.save()

        context_dict = {
            'status': "Libro Agregado!"
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_biblioteca/libros.html"
        )

    return render(request, 'app_biblioteca/libros.html')


def alumno(request):
    if request.method == 'POST':
        alumno_u = Alumno(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                      email=request.POST['email'],
                      n_libreta=request.POST['n_libreta']
                      )

        alumno_u.save()

        context_dict = {
            'status': "Alumno Agregado!"
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_biblioteca/alumno.html"
        )

    return render(request, 'app_biblioteca/alumno.html')

def profesor(request):
    if request.method == 'POST':
        profesor_u = Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                      email=request.POST['email'],
                      dni=request.POST['dni']
                      )

        profesor_u.save()

        context_dict = {
            'status': "Profesor Agregado!"
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_biblioteca/profesores.html"
        )

    return render(request, 'app_biblioteca/profesores.html')


def busqueda(request):
    context_dict = dict()
    try:
        if request.GET['name_search']:
            search_param = request.GET['name_search']
            libros = Libro.objects.filter(titulo__contains=search_param)

            context_dict = {
                'libros': libros
            }
        elif request.GET['autor_search']:
            search_param = request.GET['autor_search']
            libros = Libro.objects.filter(autor__contains=search_param)
            context_dict = {
                'libros': libros
            }
        elif request.GET['all_search']:
            search_param = request.GET['all_search']
            query = Q(titulo__contains=search_param)
            query.add(Q(autor__contains=search_param), Q.OR)
            libros = Libro.objects.filter(query)
            context_dict = {
                'libros': libros
            }




        return render(
            request=request,
            context=context_dict,
            template_name="app_biblioteca/busqueda.html",
        )




    except:
        pass






    return render(
            request=request,
            context=context_dict,
            template_name="app_biblioteca/busqueda.html",
        )
