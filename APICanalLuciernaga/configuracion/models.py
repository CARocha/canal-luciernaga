from django.db import models
from solo.models import SingletonModel
from sorl.thumbnail import ImageField

# Create your models here.

class ConocenosImg(SingletonModel):
	imagen = ImageField(upload_to='banner/conocenos',help_text='1350x280',null=True,blank=True)

	class Meta:
		verbose_name = "Imágen conócenos"