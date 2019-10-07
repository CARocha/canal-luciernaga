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
	latest_video = Video.objects.order_by('-id')[:10]
	tipo = {}
	for x in Tipo.objects.all():
		videos_list = Video.objects.filter(tipo__nombre=x).order_by('-id')
		if videos_list:
			tipo[x.nombre] = videos_list

	bann_vid = Video.objects.filter(portada=True).order_by('-id')[:3]

	return render(request,template,locals())

def news(request,template='news.html'):
	news_list = Comunicacion.objects.order_by('-id')
	thematic_list = Categoria.objects.order_by('id')
	ids = news_list.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request,template,locals())

def news_detail(request,slug,template='news_detail.html'):
	object = Comunicacion.objects.get(slug=slug)
	news_list = Comunicacion.objects.order_by('-id')
	thematic_list = Categoria.objects.order_by('id')
	ids = news_list.values_list('id',flat=True)
	common_tags = Comunicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request,template,locals())


def buscador(request,template = 'buscador.html'):
	if request.GET.get('search'):
		q = request.GET['search']
		videos = Video.objects.filter(Q(nombre__icontains = q)| Q(categoria__nombre__icontains = q)).order_by('-id')
	
	return render(request,template,locals())

