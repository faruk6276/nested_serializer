from django.urls import path,include,re_path
from . import views
from rest_framework.routers import DefaultRouter


# routers=DefaultRouter()
# routers.register('address',views.AddressView,basename='country')


urlpatterns = [
     # path('api/',include(routers.urls)),
     #path('api/country/',views.CountryViewList.as_view(),name="countrylist"),
     path('api/country/<int:pk>',views.CountryViewDetail.as_view(),name="countrydetails"),
     path('api/country/',views.CountryList.as_view()),
]
