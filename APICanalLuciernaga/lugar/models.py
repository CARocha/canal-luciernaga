# Description: Modelo de la tabla Pais
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length = 225, unique=True)
    slug = models.SlugField(max_length = 225, unique=True, editable=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        super(Pais, self).save(*args, **kwargs)

    def clean(self):
        if Pais.objects.annotate(nombre_lower=Lower('nombre')).filter(nombre_lower=self.nombre.lower()).exists():
            raise ValidationError({'nombre': 'Un país con este nombre ya existe.'})
        super(Pais, self).clean()

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
