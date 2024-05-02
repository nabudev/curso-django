from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida),
    path('despedida/', views.saludo),
]