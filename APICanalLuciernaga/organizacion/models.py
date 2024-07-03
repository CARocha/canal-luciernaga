from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from lugar.models import Pais

# Create your models here.

class Organizacion(models.Model):
	nombre = models.CharField('Nombre',max_length=200, unique=True)
	siglas = models.CharField("Siglas",help_text="Siglas o nombre corto de la oganización",max_length=200)
	logo = ImageField(upload_to='contrapartes/logos/',null=True, blank=True)
	slug = models.SlugField(max_length=200,editable=False, unique=True)
	pais = models.ForeignKey(Pais,on_delete=models.DO_NOTHING)
	correo = models.EmailField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "Organizaciones"
		verbose_name = "Organización"

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Organizacion, self).save(*args, **kwargs)

			
	
