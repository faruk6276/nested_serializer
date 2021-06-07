from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


routers=DefaultRouter()
routers.register('address',views.AddressView,basename='country')


urlpatterns = [
     path('api/',include(routers.urls)),
]
