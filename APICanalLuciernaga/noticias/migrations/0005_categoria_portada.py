# Generated by Django 2.2.3 on 2024-08-08 02:12

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_auto_20240702_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='portada',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='fotos/portadas', verbose_name='Portada'),
        ),
    ]
