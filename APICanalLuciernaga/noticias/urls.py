from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
	# path('',home,name='home'),
	path('', TemplateView.as_view(template_name = 'construccion.html')),
	path('noticias/',news,name='news'),
	path('noticias/detalles/<slug>/',news_detail,name='news_detail'),
	path('buscador-noticias/',buscador_news,name='buscador_news'),
	path('noticias/filtro/tipo/<tipo>/',filtro_tipo,name='filtro_tipo'),
	path('noticias/filtro/categoria/<categoria>/',filtro_categoria_news,name='filtro_categoria_news'),
]