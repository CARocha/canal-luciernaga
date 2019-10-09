"""APICanalLuciernaga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from APICanalLuciernaga import settings
from django.contrib.flatpages import views
from rest_framework import routers
from biblioteca.views import BibliotecaViewSet, CategoriaBibliotecaViewSet
from programacion.views import HoraProgramacionViewSet
from noticias.views import *
from videoteca.views import VideoViewSet, EpisodioViewSet,TipoVideoTecaViewSet, CategoriaVideoTecaViewSet
from lugar.views import PaisViewSet

admin.site.site_header = 'Administración Nativa Media'
admin.site.site_title = 'Nativa Media'

router = routers.DefaultRouter()
router.register('biblioteca', BibliotecaViewSet)
router.register('programacion', HoraProgramacionViewSet)
router.register('noticia', ComunicacionViewSet)
router.register('videoteca', VideoViewSet)
router.register('episodio', EpisodioViewSet)
router.register('categoria-noticia', CategoriaNoticiaViewSet)
# router.register('clasficacion-noticia', ClasificacionNoticiaViewSet)
router.register('categoria-video', CategoriaVideoTecaViewSet)
router.register('tipo-videoteca', TipoVideoTecaViewSet)
router.register('pais', PaisViewSet)
router.register('categoria-biblioteca', CategoriaBibliotecaViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('acerca/', views.flatpage, {'url': '/acerca/'}, name='acerca'),
    path('',include('noticias.urls')),
    path('videos/',include('videoteca.urls')),
    path('biblioteca/', include('biblioteca.urls')),
    path('en-directo/',include('programacion.urls')),
    path('buscador/',buscador),
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
