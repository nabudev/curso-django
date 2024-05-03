from django.urls import path
from . import views

urlpatterns = [
    #path('bienvenida/', views.bienvenida),
    #path('saludo/<str:username>', views.saludo),
    path('projects', views.project),
    #para buscar por id: path('tasks/<int:id>', views.task),
    #para buscar por nombre:
    path('tasks/<str:title>', views.task),
]