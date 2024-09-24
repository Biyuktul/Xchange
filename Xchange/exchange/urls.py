from django.urls import path, include
from . import api

urlpatterns = [
    path('/react', include('exchange.urls')),
]
