# Generated by Django 2.2.3 on 2019-08-19 18:14

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0007_comunicacion_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicacion',
            name='banner',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='banner/noticias', verbose_name='Banner'),
        ),
    ]