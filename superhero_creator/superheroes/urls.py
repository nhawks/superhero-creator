from django.urls import path

from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('details/<int:hero_id>', views.details, name = 'details'),
    path('new/', views.create, name ='create'),
    path('edit/', views.edit, name = 'edit'),
]