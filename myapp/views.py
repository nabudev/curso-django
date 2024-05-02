from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
#def bienvenida(request):
#    return HttpResponse ('Hola maquina')

#def saludo(request, username):
 #   return HttpResponse ('Hola %s' % username)

def project (request):
    projects=list(Project.objects.values())
    return JsonResponse(projects, safe= False)

def task (request, id):
    task= Tasks.objects.get(id=id)
    return HttpResponse('<h1>Task: %s</h1>' %task.title)