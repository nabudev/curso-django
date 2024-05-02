from django.urls import path
from . import views

urlpatterns = [
    #path('bienvenida/', views.bienvenida),
    path('saludo/<str:username>', views.saludo),
]