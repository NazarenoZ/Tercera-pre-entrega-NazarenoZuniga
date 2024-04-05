from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField() 
    camada = models.IntegerField()
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField()   

    def __str__(self):
        return f"Nombre: {self.nombre}    Camada: {self.camada}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, default='', null=True)
    especialidad = models.CharField(max_length=100)
    curso = models.CharField(max_length=50, default='', null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, default='', null=True)
    curso = models.CharField(max_length=50, default='', null=True)
    edad = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
class EscuelaApp(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    numero_de_telefono = models.CharField(max_length=15, default='', null=True)

    
    def __str__(self):
        return self.nombre