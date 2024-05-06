from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from django.shortcuts import render, get_object_or_404


def saludo(request):
   return render (request, 'saludo.html')
 
def index (request):
     return render(request, 'index.html')

def project (request):
    #projects=list(Project.objects.values())
    projects= Project.objects.all()
    return render (request, 'projects.html', {
        'projects': projects
    })

def task (request):
    #para buscar por id: task= get_object_or_404(Tasks, id=id)
    #para buscar por nombre:
    #task= Tasks.objects.get(title=title)
    tasks= Tasks.objects.all()
    return render (request, 'tasks.html', {
        'tasks': tasks
    })