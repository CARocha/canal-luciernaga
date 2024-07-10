from django.urls import path
from .views import *

urlpatterns = [
	path('tipo/<slug:tipo>/',list_videos, name='list_videos'),
    path('categoria/<slug:categoria>/',list_videos_categoria, name='list_videos_categoria'),
	path('detalle/<slug>/',Video_detail,name='Video_detail'),
	path('episodio/<slug:episodio>/temporada/<int:temporada>/',episodio_detail,name='episodio_detail'),
	path('ajax/video_info/',GetVideoInfo,name='get_video_info'),
]