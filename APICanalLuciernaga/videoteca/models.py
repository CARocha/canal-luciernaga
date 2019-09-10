from django.db import models
from django.utils.text import slugify
from lugar.models import Pais
from sorl.thumbnail import ImageField
from noticias.models import Categoria

#Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length = 255)
    
    class Meta:
         ordering = ['-id']

    def __str__(self):
        return self.nombre


class Director(models.Model):
    nombre = models.CharField(max_length = 255)
    # fecha_nacimiento = models.DateField('Fecha de nacimiento')

    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ['-id']


class Video(models.Model):
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    portada = models.BooleanField('Portada',default=False)
    categoria = models.ManyToManyField(Categoria,verbose_name='Categoría')
    nombre = models.CharField('Nombre',max_length = 225)
    imagen = ImageField('Imagen',upload_to='fotos/videos')
    sinopsis = models.TextField('Sinopsis')
    fecha = models.DateField('Fecha') 
    director = models.ForeignKey(Director, on_delete = models.CASCADE,verbose_name='Director')
    produccion = models.CharField('Producción',max_length = 255)
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE,verbose_name='País')
    duracion = models.CharField('Duración',max_length=20)
    url = models.URLField(null = True, blank = True)
    slug = models.SlugField(max_length = 250, unique=True, editable= False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Video, self).save(*args, **kwargs)

TEMPORADAS_CHOICE = [
    (1, 'Temporada 1'),
    (2, 'Temporada 2'),
    (3, 'Temporada 3'),
    (4, 'Temporada 4'),
    (5, 'Temporada 5'),
]

class Temporada(models.Model):
    info_video = models.ForeignKey(Video, on_delete = models.CASCADE)
    temporada = models.IntegerField(choices = TEMPORADAS_CHOICE)

    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

class Episodio(models.Model):
    temporada = models.ForeignKey(Temporada, on_delete = models.CASCADE)
    link = models.URLField(max_length = 225)
    imagen = ImageField('Imagen',upload_to='fotos/videos')
    titulo = models.CharField('Título',max_length = 225)
    sinopsis = models.TextField('Sinopsis',max_length=200)
    duracion = models.CharField('Duración',max_length=20)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Episodio"
        verbose_name_plural = "Episodios"




