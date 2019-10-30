from django.db import models
from noticias.models import Categoria
from embed_video.fields import EmbedVideoField

# Create your models here.
class Programacion(models.Model):
	titulo = models.CharField(max_length = 225)
	link = EmbedVideoField(null=True,blank=True)
	fecha = models.DateField()

	def __str__(self):
		return self.titulo
	
	class Meta:
		verbose_name = "Programación"
		verbose_name_plural = "Programaciones"

class HoraProgramacion(models.Model):
	programacion = models.ForeignKey(Programacion, on_delete = models.CASCADE)
	titulo = models.CharField(max_length = 225)
	# categoria_p = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING,null=True,verbose_name='Categoría')
	descripcion = models.TextField("Descripción", blank=True, null=True)
	hora_inicio = models.TimeField()
	hora_fin = models.TimeField()

	class Meta:
		verbose_name ="Hora Programación"
		verbose_name_plural ="Horas de programacion"

	def __str__(self):
		return self.titulo
		
	