from django.db import models

class Alumnos(models.Model):#Define la estructura de la tabla
    matricula = models.CharField( max_length=12) #texto corto
    nombre = models.TextField()#Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)#fecha y tiempo
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        ordering=["-created"]
    #el - indica que se ordenara del mas reciente al mas viejo
    def __str__(self):
        return self.nombre
    
    class Alumnos(models.Model):
        matricula=models.CharField(max_length=12, verbose_name= "Mat")
