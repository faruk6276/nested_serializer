from .models import *
from rest_framework import serializers
from .models import *

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model=Address
        fields=['id','address']

class CitySerializer(serializers.ModelSerializer):
    city_address=AddressSerializer(many=True, read_only=True)
    class Meta:
        model=City
        fields=['id','city_name','city_address']

class CountrySerializer(serializers.ModelSerializer):
    country_city=CitySerializer(many=True,read_only=True)
    class Meta:
        model=Country
        fields=['id','country_name','country_city']