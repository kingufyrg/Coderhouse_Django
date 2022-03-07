import datetime
import random
from django.http import HttpResponse
from django.template import Template,Context


def saludo(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos el uso de las vistas")


def dia(request):
    dia = datetime.datetime.now()
    documento = f"Hoy es día: <br> {dia}"

    return HttpResponse(documento)


def numero_random(request):
    numero = random.randrange(15,180)
    texto = f'<h1>Este es tu número random: {numero}</h1>'
    return HttpResponse(texto)


def numero_del_usuario(request,numero):
    texto = f'<h1>Este es tu número: {numero}</h1>'
    return HttpResponse(texto)


def nacimiento(request, numero):
    edad = int(datetime.datetime.now().year) - numero
    texto = f'<h1>Este es tu edad: {edad}</h1>'
    return HttpResponse(texto)


def mi_plantilla(request):
    plantilla = open('/Users/yairrobledo/Documents/Git/Proyecto/miproyecto/miproyecto/plantillas/plantilla.html')
    template = Template(plantilla.read())
    context = Context()
    plantilla_preparada = template.render(context)
    return HttpResponse(plantilla_preparada)

