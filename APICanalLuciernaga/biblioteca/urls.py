from django.urls import path
from .views import *

urlpatterns = [
	path('',Biblioteca_list,name='biblioteca_list'),
	path('buscar/', buscador_biblioteca, name='buscador_biblioteca'),
	path('filtro-categoria/<slug>/', filtro_categoria, name='filtro_categoria'),
]
