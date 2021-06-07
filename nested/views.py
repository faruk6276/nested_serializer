from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class AddressView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer