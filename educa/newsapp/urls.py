from django.urls import path
from .views import bbc

urlpatterns = [
path('bbc/', bbc, name = 'BBC')

]