from enum import Enum
from django.db import models
from solo.models import SingletonModel
from sorl.thumbnail import ImageField

# Create your models here.

class ConocenosImg(SingletonModel):
	imagen = ImageField(upload_to='banner/conocenos',help_text='1350x280',null=True,blank=True)

	class Meta:
		verbose_name = "Imágen conócenos"

class NoticiaImg(SingletonModel):
	imagen = ImageField(upload_to='banner/conocenos',help_text='1350x280',null=True,blank=True)

	class Meta:
		verbose_name = "Imágen de noticias"
# class Opciones(Enum):
#     IMAGEN = "IMAGEN"
#     VIDEO = "VIDEO"
#     YOUTUBE = "YOUTUBE"

#     @classmethod
#     def choices(cls):
#         return tuple((obj.name, obj.value) for obj in cls)

choices = ((1, 'IMAGEN'), (2, 'YOUTUBE'))

class BannerSitio(SingletonModel):
    tipo = models.IntegerField(choices=choices, default=1)
    titulo = models.CharField(max_length=250, blank=True, null=True)
    descripcion = models.TextField(null=True,blank=True)
    youtube_link = models.CharField(max_length=250,
                                    null=True,
                                    blank=True)
    def __str__(self):
        return str(self.tipo)
    class Meta:
        verbose_name = "Banner sitio"
        verbose_name_plural = "Banner sitio"
class InlinesImages(models.Model):
    banner = models.ForeignKey('BannerSitio', on_delete=models.CASCADE)
    titulo_img = models.CharField(max_length=250)
    descripcion_img = models.TextField(null=True,blank=True)
    imagen = ImageField(upload_to='banner/conocenos',
                        help_text='1350x800',
                        null=True,
                        blank=True)

    def __str__(self):
        return self.titulo_img
    class Meta:
        verbose_name = "Imagenes"
        verbose_name_plural = "Imagenes"