from django.db import models
from django.utils.text import slugify
from taggit_autosuggest.managers import TaggableManager
from lugar.models import Pais
from sorl.thumbnail import ImageField
from usuario.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length =225)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

# class Clasificacion(models.Model):
#     nombre = models.CharField(max_length = 225)
    
#     def __str__(self):
#         return self.nombre
    
#     class Meta:
#         verbose_name = "Clasificacion"
#         verbose_name_plural = "Clasificaciones"
        

TIPO_COMUNICACION_CHOICE = [
    (1, 'Noticia'),
    (2, 'Reportaje'),
]

class Comunicacion(models.Model):
    tipo = models.IntegerField(choices = TIPO_COMUNICACION_CHOICE)
    ultimo_momento = models.BooleanField(default=False)
    portada = models.BooleanField('Portada',default=False)
    titulo = models.CharField(max_length = 225)
    # clasificacion = models.ForeignKey(Clasificacion, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha = models.DateField()
    banner = ImageField('Banner',upload_to='banner/noticias',null=True,blank=True)
    foto = ImageField('Imagen',upload_to='fotos/noticias')
    descripcion = models.TextField()
    pais = models.ForeignKey(Pais, on_delete = 255)
    fuente = models.CharField(max_length = 225)
    tags = TaggableManager(blank=True)
    slug = models.SlugField(max_length=250, unique=True, editable= False)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Noticia/Reportaje"
        verbose_name_plural = "Noticias/Reportajes"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Comunicacion, self).save(*args, **kwargs)
    