from django.db import models

# Create your models here.

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    last_name_2 = models.CharField(max_length=100, blank=True, null=True)

    cedula = models.CharField(max_length=20, default='000-0000000-0')

    fecha_nacimiento = models.DateField(default='1900-01-01')

    sexo = models.BinaryField(default=None, blank=True, null=True)
    
    address = models.CharField(max_length=300)

    email = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    city = models.CharField(max_length=255)

    province = models.CharField(max_length=200)

    country = models.CharField(max_length=125)

    def __str__(self) -> str:
        return self.first_name + "   " + self.last_name