from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ComunicacionSerializer, CategoriaSerializer

from videoteca.models import *
from django.db.models import Q

# Create your views here.
class ComunicacionViewSet(viewsets.ModelViewSet):
    queryset = Comunicacion.objects.all()
    serializer_class = ComunicacionSerializer

class CategoriaNoticiaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# class ClasificacionNoticiaViewSet(viewsets.ModelViewSet):
#     queryset = Clasificacion.objects.all()
#     serializer_class = ClasificacionSerializer


# Web Views
def home(request,template='index.html'):
	highlight_news = Comunicacion.objects.filter(ultimo_momento=1,tipo=1)[:5]

	#lo nuevo
	latest_video = Video.objects.order_by('-id')[:10]
	dict = {}
	for x in latest_video:
		similares = Video.objects.filter(tipo = x.tipo,categoria__in = x.categoria.all()).exclude(id = x.id)
		dict[x] = similares

	#resto de tipos
	tipo = {}
	for x in Tipo.objects.all():
		videos_list = Video.objects.filter(tipo__nombre=x).order_by('-id')[:15]
		videos = {}
		for vid in videos_list:
			similares = Video.objects.filter(tipo = vid.tipo,categoria__in = vid.categoria.all()).exclude(id = vid.id)
			videos[vid] = similares
		if videos_list:
			tipo[x.nombre] = videos
	####

	bann_vid = Video.objects.filter(portada=True).order_by('-id')[:3]

	return render(request,template,locals())

def news(request,template='news.html'):
	news_list = Comunicacion.objects.order_by('-id')
	thematic_list = Categoria.objects.filter(id__in = news_list.values_list('categoria',flat=True)).order_by('id')
	banner = Comunicacion.objects.filter(portada = True).order_by('-id')[:3]
	ids = news_list.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request,template,locals())

def news_detail(request,slug,template='news_detail.html'):
	object = Comunicacion.objects.get(slug=slug)
	news_list = Comunicacion.objects.order_by('-id')
	thematic_list = Categoria.objects.filter(id__in = news_list.values_list('categoria',flat=True)).order_by('id')
	ids = news_list.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request,template,locals())

def filtro_tipo(request,tipo,template='news.html'):
	news_list = Comunicacion.objects.filter(tipo = tipo).order_by('-id')
	thematic_list = Categoria.objects.filter(id__in = news_list.values_list('categoria',flat=True)).order_by('id')
	banner = Comunicacion.objects.filter(tipo = tipo,portada = True).order_by('-id')[:3]
	ids = news_list.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request,template,locals())

def filtro_categoria_news(request,categoria,template='news.html'):
	news_list = Comunicacion.objects.filter(categoria__slug = categoria).order_by('-id')
	thematic_list = Categoria.objects.filter(id__in = news_list.values_list('categoria',flat=True)).order_by('id')
	banner = Comunicacion.objects.filter(categoria__slug = categoria,portada = True).order_by('-id')[:3]
	ids = news_list.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	
	return render(request,template,locals())

def buscador_news(request,template='news.html'):
	general = Comunicacion.objects.order_by('-id')
	thematic_list = Categoria.objects.filter(id__in = general.values_list('categoria',flat=True)).order_by('id')
	ids = general.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	
	if request.GET.get('search'):
		q = request.GET['search']
		news_list = Comunicacion.objects.filter(Q(titulo__icontains = q)| Q(categoria__nombre__icontains = q)
												| Q(pais__nombre__icontains = q)| Q(descripcion__icontains = q)).order_by('-id')

	return render(request,template,locals())

def buscador(request,template = 'buscador.html'):
	if request.GET.get('search'):
		q = request.GET['search']
		videos = Video.objects.filter(Q(nombre__icontains = q)| Q(categoria__nombre__icontains = q)).order_by('-id')
	
	return render(request,template,locals())
