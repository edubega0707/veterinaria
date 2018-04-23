from django.db import models


ANIMAL_CATEGORIA_CHOICES=(
    ('asd','as'),
)

STATUS_CANDIDATO=(
    ('M','MASCOTA'),
    ('O','OBVINOS'),
    ('S','SIN ATENDER')
)
class Animal(models.Model):
    nombre_animal          =models.CharField(max_length=100,blank=True,null=True)
    raza_animal            =models.CharField(max_length=100, blank=True, null=True)
    categoria_animal       =models.CharField(max_length=100, blank=True, null=True, choices=ANIMAL_CATEGORIA_CHOICES )
    peso_animal            =models.IntegerField(blank=True, null=True)
    edad_animal            =models.IntegerField(blank=True, null=True)
    foto_animal            =models.ImageField(upload_to='images', blank=True, null=True)
