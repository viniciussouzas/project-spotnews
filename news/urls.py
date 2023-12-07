from django.urls import path
from .views import home


urlpatterns = [
    path('', index, name='home-page'),
]
