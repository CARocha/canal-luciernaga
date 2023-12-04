from django.db import models
from sorl.thumbnail import ImageField
from noticias.models import Categoria
from sorl.thumbnail import ImageField
from django.utils.safestring import mark_safe
from noticias.models import Categoria
# Create your models here.


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=225)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=255)
    foto = ImageField('Imagen', upload_to='fotos/biblioteca')
    archivo = models.FileField(upload_to='documento/biblioteca')

    def __str__(self):
        return self.nombre

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.foto))

    image_tag.short_description = 'Imagen'
    class Meta:
        verbose_name = "Biblioteca"
        verbose_name_plural = "Bibliotecas"