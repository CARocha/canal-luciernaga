from django.contrib import admin, messages
from .models import *

class PaisAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if Pais.objects.filter(nombre=obj.nombre).exists() and not change:
            messages.error(request, f"El país '{obj.nombre}' ya existe.")
            return
        else:
            super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PaisAdmin, self).get_form(request, obj, **kwargs)
        if form and 'slug' in form.base_fields:
            form.base_fields['slug'].widget.attrs['readonly'] = True  # Hace el campo slug de solo lectura en el admin
        return form

    search_fields = ['nombre']
    prepopulated_fields = {"slug": ("nombre",)}


# Register your models here.
admin.site.register(Pais, PaisAdmin)