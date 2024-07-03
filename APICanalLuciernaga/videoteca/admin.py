from django.contrib import admin
from .models import Video, Director, Tipo, Episodio, Temporada
from lugar.models import Pais
import nested_admin

class TipoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    
class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class EpisodioInline(nested_admin.NestedStackedInline):
    model = Episodio
    extra = 1

class TemporadaInline(nested_admin.NestedStackedInline):
    model = Temporada
    extra = 1
    inlines = [EpisodioInline]


class VideoAdmin(nested_admin.NestedModelAdmin):
    autocomplete_fields = ['tipo','director','categoria', 'pais']
    inlines = [TemporadaInline,]
    list_display = ['nombre','fecha','director','url','image_tag']
    list_filter = ('pais','tipo','categoria')
    search_fields = ['nombre','pais__nombre','tipo__nombre']
    list_per_page = 15

    class Media:
        js = ('js/video/ocultar.js',)
    

# Register your models here.
admin.site.register(Tipo,TipoAdmin)
# admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Director,DirectorAdmin) 
admin.site.register(Video,VideoAdmin)  