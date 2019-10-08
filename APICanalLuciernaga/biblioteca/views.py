from django.shortcuts import render
from rest_framework import viewsets
from .models import Biblioteca, Categoria
from .serializers import BibliotecaSerializer, CategoriaSerializer
from django.db.models import Q

# Create your views here.

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer 

class CategoriaBibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

def Biblioteca_list(request,template='biblioteca.html'):
	b_list = Biblioteca.objects.order_by('-id')
	cats = Categoria.objects.filter(id__in = b_list.values_list('categoria',flat=True))
	return render(request,template,locals())

def buscador_biblioteca(request,template='biblioteca.html'):
	general = Biblioteca.objects.order_by('-id')
	cats = Categoria.objects.filter(id__in = general.values_list('categoria',flat=True))
	
	if request.GET.get('search'):
		q = request.GET['search']
		b_list = Biblioteca.objects.filter(Q(nombre__icontains = q)| Q(categoria__nombre__icontains = q)).order_by('-id')

	return render(request,template,locals())

def filtro_categoria(request,slug,template='biblioteca.html'):
	b_list = Biblioteca.objects.filter(categoria__slug = slug).order_by('-id')

	general = Biblioteca.objects.order_by('-id')
	cats = Categoria.objects.filter(id__in = general.values_list('categoria',flat=True))
	return render(request,template,locals())
