from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('data', new_data, name = 'new_data'),
]