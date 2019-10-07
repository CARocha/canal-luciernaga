from django.urls import path
from .views import *

urlpatterns = [
	path('<tipo>/',list_videos, name='list_videos'),
	path('detalle/<slug>/',Video_detail,name='Video_detail'),
	path('detalle/<slug>/temporada/<temporada>/episodio/<episodio>/',episodio_detail,name='episodio_detail'),
	path('ajax/video_info/',GetVideoInfo,name='get_video_info'),
]