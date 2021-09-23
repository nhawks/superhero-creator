from django.urls import path

from . import views

app_name = 'superheroes'
urlspatterns = [
    path('index', views.index, name = 'index')
]