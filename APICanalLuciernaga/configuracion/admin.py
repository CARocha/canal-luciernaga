from django.contrib import admin
from .models import *
from solo.admin import SingletonModelAdmin

# Register your models here.
admin.site.register(ConocenosImg,SingletonModelAdmin)