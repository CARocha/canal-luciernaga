from django.contrib import admin
from .models import Organizacion

# Register your models here.
class OrganizacionAdmin(admin.ModelAdmin):
    search_fields = ['nombre','siglas']
    list_filter = ('pais__nombre',)
    list_display = ['nombre','siglas','pais','correo']

admin.site.register(Organizacion, OrganizacionAdmin)

