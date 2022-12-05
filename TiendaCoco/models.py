from django.db import models

# Create your models here.
#model1
class Tienda(models.Model):
    producto= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=200)
    precio= models.IntegerField()

    def __str__ (self) -> str:
        return f"{self.producto} ({self.descripcion}) ->(${self.precio})"

#model2
class Comprador(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    dni= models.IntegerField()
   

    def __str__ (self) -> str:
        return f"{self.nombre} {self.apellido} ({self.dni})"

#model3
class Vendedor(models.Model):
    empresa= models.CharField(max_length=50)
    direccion= models.CharField(max_length=100)
    

    def __str__ (self) -> str:
        return f"{self.empresa} ({self.direccion})"