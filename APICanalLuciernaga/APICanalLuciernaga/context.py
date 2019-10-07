from programacion.models import *
import datetime 
from videoteca.models import *

def directo(request):
	hoy = datetime.date.today()
	hora = datetime.datetime.now().strftime('%H:%M:%S')

	en_vivo = Programacion.objects.filter(fecha = hoy,link__isnull = False,horaprogramacion__hora_fin__gte = hora)

	if en_vivo:
		result = True
	else: 
		result = False
		
	return {'directo' : result,}

def tipos_video(request):
	videos = Video.objects.values_list('tipo',flat = True)
	tipos = Tipo.objects.filter(id__in = videos)

	return {'tipos':tipos}