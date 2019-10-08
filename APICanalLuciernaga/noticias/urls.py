from django.urls import path
from .views import *

urlpatterns = [
	path('',home,name='home'),
	path('noticias/',news,name='news'),
	path('noticias/detalles/<slug>/',news_detail,name='news_detail'),
	path('buscador-noticias/',buscador_news,name='buscador_news'),
]