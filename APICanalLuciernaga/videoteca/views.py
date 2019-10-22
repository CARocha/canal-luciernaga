from rest_framework import viewsets
from .models import *
from .serializers import VideoSerializer, EpisodioSerializer, CategoriaSerializer, TipoSerializer
from django.shortcuts import render
from django.http import JsonResponse
from .forms import *

class VideoViewSet(viewsets.ModelViewSet):
	queryset = Video.objects.all()
	serializer_class  = VideoSerializer

class EpisodioViewSet(viewsets.ModelViewSet):
	queryset = Episodio.objects.all()
	serializer_class = EpisodioSerializer

class CategoriaVideoTecaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

class TipoVideoTecaViewSet(viewsets.ModelViewSet):
	queryset = Tipo.objects.all()
	serializer_class = TipoSerializer

def list_videos(request,tipo,template='movies.html'):
	name = Tipo.objects.get(slug = tipo)

	if request.method == 'POST':
		form = CategoriasFilter(request.POST,tipo = tipo)
		if form.is_valid():
			cate = form.cleaned_data['categorias']
			cat = {}
			for x in Categoria.objects.filter(id = cate.id):
				videos_list = Video.objects.filter(categoria=x,tipo__slug=tipo).order_by('-id')
				videos = {}
				for vid in videos_list:
					similares = Video.objects.filter(tipo = vid.tipo,categoria__in = vid.categoria.all()).exclude(id = vid.id)
					videos[vid] = similares
				if videos_list:
					cat[x] = videos
	else:
		form = CategoriasFilter(tipo = tipo)
		cat = {}
		for x in Categoria.objects.all():
			videos_list = Video.objects.filter(categoria=x,tipo__slug=tipo).order_by('-id')
			videos = {}
			for vid in videos_list:
				similares = Video.objects.filter(tipo = vid.tipo,categoria__in = vid.categoria.all()).exclude(id = vid.id)
				videos[vid] = similares
			if videos_list:
				cat[x] = videos

	return render(request,template,locals())

def Video_detail(request,slug,template='detail_movie.html'):
	object = Video.objects.get(slug=slug)
	if object.tipo.nombre == 'Series':
		episodio = Episodio.objects.filter(temporada__info_video = object).order_by('id').first()
		temporadas = Temporada.objects.filter(info_video = object)
	return render(request,template,locals())

def episodio_detail(request,slug,temporada,episodio,template='detail_episodio.html'):
	episodio = Episodio.objects.get(temporada__info_video__slug = slug,temporada__temporada = temporada,slug=episodio)
	temporadas = Temporada.objects.filter(info_video__slug = slug)

	return render(request,template,locals())

def GetVideoInfo(request):
	if request.method == "GET" and request.is_ajax():
		video_id = request.GET.get("video_id")
		try:
			video = Video.objects.get(id = video_id)
			print (video.categoria)
		except:
			return JsonResponse({"success":False}, status=400)
		video_info = {
			# "categoria":video.categoria.nombre,
			"nombre":video.nombre,
			"sinopsis":video.sinopsis,
			"fecha":video.fecha,
			# "director":video.director,
			"produccion":video.produccion,
			"pais":video.pais.nombre,
			"duracion":video.duracion,
			"url": video.url
		}
		return JsonResponse({"video_info":video_info}, status=200)
	return JsonResponse({"success":False}, status=400)




