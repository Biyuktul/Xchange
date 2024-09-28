from django.urls import path, include

from .api import hi_api, run_scraper_view


urlpatterns = [
    path('api/', hi_api, name='hi_api'),
    path('run-scraper/', run_scraper_view, name='run_scraper'),
]
