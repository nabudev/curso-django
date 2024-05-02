from django.db import models

# Create your models here.

class Project(models.Model):
    name= models.CharField(max_length=200)
    
    

#creando una tabla relacionada con project    
class Tasks(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField()
    #clave foranea, entre parentesis el nombre de la tabla a la que pertenece y seguido de la coma la config de como se modificara si se eliminan atributos de la tabla project
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
