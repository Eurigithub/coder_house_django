from django.db import models

# Create your models here.
class Clientes (models.Model):
    nombre=models.CharField(max_length=20,null=False,blank=False)
    apellido=models.CharField(max_length=60,null=False,blank=False)
    numerodetel=models.IntegerField(max_length=20)
    email=models.EmailField()
    numeroDNI=models.IntegerField(max_length=10)

class Compras(models.Model):
    numerodeitem=models.IntegerField(max_length=6)
    fechadecompra=models.DateField()
    item=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.nombre

