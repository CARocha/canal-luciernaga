# Generated by Django 2.2.3 on 2024-07-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0006_auto_20240702_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='slug',
            field=models.SlugField(editable=False, max_length=250),
        ),
        migrations.AlterField(
            model_name='episodio',
            name='titulo',
            field=models.CharField(max_length=225, verbose_name='Título'),
        ),
    ]
