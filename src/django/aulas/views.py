#from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from .models import Musician, Album


# Create your views here.
def hello(request):
    return HttpResponse("Hola mundo desde Django")

def goodbye(request):
    return HttpResponse("Adiós mundo desde Django")

def edad(request, anios, futuro):
    incremento = futuro - date.today().year 
    cumplira = anios + incremento
    mensaje = "En el año %d tendrás %d años" %(futuro,cumplira)

    return HttpResponse(mensaje)

def primera_plantilla(request):
    
    tpl = get_template("primera_plantilla.html")

    ctx = Context(
        
    )

    mensaje = tpl.render ({
            'nombre': 'Juan'
        })

    return HttpResponse(mensaje)


def segunda_plantilla(request):
    
    tpl = get_template("segunda_plantilla.html")

    ctx = Context(
        
    )

    mensaje = tpl.render ({
            'nombre': 'Martín',
            'fecha': date.today()
        })

    return HttpResponse(mensaje)
    

def tercera_plantilla(request):
    
    tpl = get_template("tercera_plantilla.html")

    

    return render(request, "tercera_plantilla.html", {
        'nombre': 'Lucía',
        'fecha': date.today()
    })
       


class Empleado (object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido    


def cuarta_plantilla(request):
    
    empleado = Empleado("Carlos", "Santana")
    
    laborables = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

    return render(request, "cuarta_plantilla.html", {
        'mi_empleado': empleado,
        'fecha_actual': date.today(),
        'dias_laborables': laborables
    })    


def crear_musico(request, nombre, apellido, instrumento):
    per = Musician(first_name=nombre, last_name=apellido, instrument=instrumento)
    per.save()
    mensaje = "Músico creado: %s %s, Instrumento: %s" % (nombre, apellido, instrumento)
    return HttpResponse(mensaje)
    return render(request, "crear_persona.html")

def crear_album(request, nombre, estrellas,artista_id):
    art=Musician.objects.get(id=artista_id)
    album = Album(name=nombre, release_date=date.today(), num_stars=estrellas, artist=art)
    art.save()
    mensaje = "Album creado: %s %s, del artista: %s" % (album.name, art.last_name, album.id)
    return HttpResponse(mensaje)
    return render(request, "crear_persona.html")