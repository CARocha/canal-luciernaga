from django.contrib import admin
from .models import *
from lugar.models import Pais

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

# class ClasificacionAdmin(admin.ModelAdmin):
#     search_fields = ['nombre']
    
class PaisAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class ComunicacionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['categoria','pais' ]
    
    class Media:
        js = ('js/noticia/check.js',)

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
# admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Comunicacion, ComunicacionAdmin)

#paginas estaticas
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
 
class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = FlatPage
        fields = '__all__'
 
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm
 
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)