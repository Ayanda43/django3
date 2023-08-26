from django.db import models

# Create your models here.

class users(models.Model):
    name= models.CharField(max_length=10)
    surname = models.CharField(max_length=10)

class dataset(models.Model):
    date= models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    temperature = models.DecimalField(max_digits=10, decimal_places=1)
    humidity = models.DecimalField(max_digits=10, decimal_places=1)