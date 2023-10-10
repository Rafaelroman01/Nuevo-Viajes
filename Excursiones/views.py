from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def vista_saludo(request):
    return HttpResponse("Hola-Bienvenidos")

def vista_plantilla(request):
    listado_prueba = ["Excursion Rosario", "Excursion Santa Fe", "Excursion San Nicolas", "Excursion Bariloche", "Excursion Buenos Aires", "Excursion La Plata", "Excursion Misiones", "Excursion Iguazu", "Excursion San Martin de los Andes" ]
    datos = {"excursiones": "Argentina", "listado_prueba": listado_prueba}
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)