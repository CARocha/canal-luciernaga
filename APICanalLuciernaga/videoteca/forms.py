# from dal import autocomplete
from django import forms
from .models import *
from noticias.models import Categoria

def categorias(tipo):   
	foo = Video.objects.filter(tipo__slug=tipo).values_list('categoria',flat=True)
	return Categoria.objects.filter(id__in = foo)

def tipos(categoria):   
	foo = Video.objects.filter(categoria__slug=categoria).values_list('tipo',flat=True)
	return Tipo.objects.filter(id__in = foo)

class CategoriasFilter(forms.Form):
	def __init__(self, *args, **kwargs):
		tipo = kwargs.pop("tipo")
		super(CategoriasFilter, self).__init__(*args, **kwargs)
		self.fields['categorias'] = forms.ModelChoiceField(queryset=categorias(tipo), required=True, label=u'Categorias')
class TiposFilter(forms.Form):
	def __init__(self, *args, **kwargs):
		categoria = kwargs.pop("categoria")
		super(TiposFilter, self).__init__(*args, **kwargs)
		self.fields['tipos'] = forms.ModelChoiceField(queryset=tipos(categoria), required=True, label=u'Tipos')