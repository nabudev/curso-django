from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from django.shortcuts import render, get_object_or_404


def saludo(request):
   return render (request, 'saludo.html')
 
def index (request):
     return render(request, 'index.html')

def project (request):
    projects=list(Project.objects.values())
    return JsonResponse(projects, safe= False)

def task (request, title):
    #para buscar por id: task= get_object_or_404(Tasks, id=id)
    #para buscar por nombre:
    task= Tasks.objects.get(title=title)
    return HttpResponse('<h1>Task: %s</h1>' %task.title)