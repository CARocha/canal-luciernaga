from django.db import models
from django.contrib.auth.models import AbstractUser
from organizacion.models import *

from sorl.thumbnail import ImageField

# Create your models here.
class User(AbstractUser):
	org = models.ForeignKey(Organizacion,on_delete=models.DO_NOTHING,null=True,blank=True)
	avatar = ImageField(upload_to='usuario/avatar/',null=True,blank=True)

	def __str__(self):
		return self.username

	class Meta(object):
		unique_together = ('email','username')
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'
