# Generated by Django 2.2.3 on 2019-08-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0003_auto_20190808_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='duracion',
            field=models.CharField(max_length=20, verbose_name='Duración'),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='sinopsis',
            field=models.TextField(max_length=200, verbose_name='Sinopsis'),
        ),
    ]