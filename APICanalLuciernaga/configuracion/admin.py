from django.contrib import admin
from .models import *
from solo.admin import SingletonModelAdmin

# Register your models here.
class InlinesImagesInline(admin.TabularInline):
    model = InlinesImages
    extra = 1

class BannerSitioAdmin(SingletonModelAdmin):
    inlines = (InlinesImagesInline,)
    list_display = ('titulo','tipo')
    list_filter = ('tipo',)
    
    class Media:
        js = ('js/admin/banner.js',)

admin.site.register(ConocenosImg,SingletonModelAdmin)
admin.site.register(BannerSitio,BannerSitioAdmin)