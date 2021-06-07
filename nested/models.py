from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name
    

class City(models.Model):
    country=models.ForeignKey(Country, on_delete=models.CASCADE,related_name='country_city')
    city_name = models.CharField( max_length=50)

    def __str__(self):
        return self.city_name

class Address(models.Model):
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='city_address')
    address = models.CharField( max_length=50)
    

    def __str__(self):
        return self.address