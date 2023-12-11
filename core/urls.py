from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, uptade, delete

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name='editar'),
    path('uptade/<int:id>', uptade, name='uptade'),
    path('delete/<int:id>', delete, name='delete'),
]