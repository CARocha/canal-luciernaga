# Description: Modelo de la tabla Pais
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length = 225)
    slug = models.SlugField(max_length = 225, unique=True, editable=False)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Pais, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
