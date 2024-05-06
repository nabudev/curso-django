from django.db import models

# Create your models here.

class Project(models.Model):
    name= models.CharField(max_length=200)
    #creo un metodo para que en mi panel de admin aparezcan las tareas por sus nombres reales
    def __str__(self):
        return self.name
    
    

#creando una tabla relacionada con project    
class Tasks(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField()
    #clave foranea, entre parentesis el nombre de la tabla a la que pertenece y seguido de la coma la config de como se modificara si se eliminan atributos de la tabla project
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' - ' + self.project.name
