from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse ('Hola maquina')

def saludo(request):
    return HttpResponse ('nos vemos maquina')


