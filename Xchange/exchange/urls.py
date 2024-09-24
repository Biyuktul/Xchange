from django.urls import path, include

from .api import hi_api


urlpatterns = [
    path('api/', hi_api, name='hi_api'),
]
