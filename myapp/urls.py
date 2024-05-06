from django.urls import path
from . import views

urlpatterns = [
    path('saludo', views.saludo),
    path('projects', views.project),
    path('tasks/<str:title>', views.task),
    path('', views.index)
]