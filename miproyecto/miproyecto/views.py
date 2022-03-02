import datetime

from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos el uso de las vistas")


def dia(request):
    dia = datetime.datetime.now()
    documento = f"Hoy es día: <br> {dia}"

    return HttpResponse(documento)
