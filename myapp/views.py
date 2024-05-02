from django.http import HttpResponse

#def bienvenida(request):
#    return HttpResponse ('Hola maquina')

def saludo(request, username):
    return HttpResponse ('Hola %s' % username)


