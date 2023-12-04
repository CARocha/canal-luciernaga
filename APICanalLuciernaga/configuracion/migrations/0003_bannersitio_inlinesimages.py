# Generated by Django 2.2.3 on 2023-12-03 05:10

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20191029_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerSitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'IMAGEN'), (2, 'YOUTUBE')], default=1)),
                ('titulo', models.CharField(blank=True, max_length=250, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Banner sitio',
                'verbose_name_plural': 'Banner sitio',
            },
        ),
        migrations.CreateModel(
            name='InlinesImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_img', models.CharField(max_length=250)),
                ('descripcion_img', models.TextField(blank=True, null=True)),
                ('imagen', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x800', null=True, upload_to='banner/conocenos')),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.BannerSitio')),
            ],
            options={
                'verbose_name': 'Imagenes',
                'verbose_name_plural': 'Imagenes',
            },
        ),
    ]
