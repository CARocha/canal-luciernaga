from django.contrib import admin, messages
from .models import *

class PaisAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if Pais.objects.filter(nombre=obj.nombre).exists() and not change:
            messages.error(request, f"El país '{obj.nombre}' ya existe.")
        else:
            obj.save()
    search_fields = ['nombre']


# Register your models here.
admin.site.register(Pais, PaisAdmin)