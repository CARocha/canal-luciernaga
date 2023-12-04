from django.contrib import admin
from .models import Biblioteca

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class BibliotecaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['categoria']
    list_display = ['nombre',
                    'categoria',
                    'image_tag',
                    'archivo']
    list_filter = ('categoria__nombre',)
    search_fields = ['nombre']

admin.site.register(Biblioteca,BibliotecaAdmin)
# admin.site.register(Categoria,CategoriaAdmin)