from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reparacion(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada {self.camada}"

class Proveedor(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6)
    nombre= models.CharField(max_length=30)
    telefono= models.CharField(max_length=30)           
    email= models.EmailField()              
    direccion= models.CharField(max_length=30)          
    observaciones = models.CharField(max_length=140)
    def __str__(self):
        return f"Codigo: {self.codigo} - Nombre: {self.nombre} - Telefono {self.telefono} - E-Mail {self.email} - Direccion {self.direccion} - Observaciones {self.observaciones}"

class Cliente(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6) 
    nombre= models.CharField(max_length=30)   
    apellido= models.CharField(max_length=30)    
    telefono= models.CharField(max_length=30)           
    email= models.EmailField()              
    direccion= models.CharField(max_length=30)          
    observaciones = models.CharField(max_length=140)

    def __str__(self):
        return f"Codigo: {self.codigo} - Nombre: {self.nombre} - Apellido {self.apellido} - Telefono {self.telefono} - E-Mail {self.email} - Direccion {self.direccion} - Observaciones {self.observaciones}"

class Repuesto(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6) 
    numero_de_parte= models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30) 
    precio_de_costo= models.CharField(max_length=30)
    stock = models.CharField(max_length=30)
    proveedor = models.CharField(max_length=30)
    observaciones = models.CharField(max_length=140)

    def __str__(self):
        return f"Codigo: {self.codigo} - Numero de parte: {self.numero_de_parte} - Descripcion {self.descripcion} - precio de costo {self.precio_de_costo} - Stock {self.stock} - Proveedor {self.proveedor} - Observaciones {self.observaciones}"

# Clase 24
class Avatar(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"