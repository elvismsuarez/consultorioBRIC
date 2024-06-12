from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Record(models.Model):

    sex_list = [
        ("Hombre", "Hombre"),
        ("Mujer", "Mujer")

    ]

    country_list =[
        ("Dominican Republic", "Dominican Republic"),
        ("Haiti", "Haiti"),
        ("Jamaica", "Jamaica"),
        ("USA", "USA"),
        ("Costa Rica", "Costa Rica"),
        ("Paraguay", "Paraguay")
    ]

    input_type = 'date'

    creation_date = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    last_name_2 = models.CharField(max_length=100, blank=True, null=True)

    cedula = models.CharField(max_length=20, default='000-0000000-0')

    fecha_nacimiento = models.DateField()

    sexo = models.CharField(max_length=10, choices=sex_list, null=False)
    
    address = models.CharField(max_length=300)

    numero_record = models.CharField(max_length=50, blank=True, null=True)

    nombre_padre = models.CharField(max_length=100, blank=True, null=True)

    direccion_padre = models.CharField(max_length=300, blank=True, null=True)

    nombre_madre = models.CharField(max_length=100, blank=True, null=True)

    direccion_madre = models.CharField(max_length=300, blank=True, null=True)

    nombre_conyuge = models.CharField(max_length=100, blank=True, null=True)

    fecha = models.DateTimeField(default=datetime.now, auto_now=False, auto_now_add=False)

    observaciones = models.CharField(max_length=500, blank=True, null=True)
    
    email = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    city = models.CharField(max_length=255)

    province = models.CharField(max_length=200)

    country = models.CharField(max_length=125, choices=country_list)

    def __str__(self) -> str:
        return self.first_name + "   " + self.last_name