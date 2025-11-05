#from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

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
       
    