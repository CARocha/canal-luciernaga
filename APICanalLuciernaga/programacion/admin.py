from django.contrib import admin
from .models import Programacion, HoraProgramacion

# Register your models here.
class HoraProgramacionInline(admin.StackedInline):
    model = HoraProgramacion
    extra = 1

class ProgramacionAdmin(admin.ModelAdmin):
    inlines = [HoraProgramacionInline,]
    search_fields = ['titulo']
    list_display = ['titulo','fecha','link']
    list_filter = ('fecha',)

admin.site.register(Programacion, ProgramacionAdmin)