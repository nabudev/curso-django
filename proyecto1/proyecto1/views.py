from django.http import HttpResponse

#creamos una vista
def saludo (request):
    return HttpResponse("Hola")

#creamos otra vista
def despedida(request):
    return HttpResponse("Chau")

#las vistas deben estar especificadas en el archivo url.py