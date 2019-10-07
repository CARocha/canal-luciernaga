# Generated by Django 2.2.3 on 2019-10-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0002_remove_director_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='temporada',
            name='temporada',
            field=models.IntegerField(choices=[(1, 'Temporada 1'), (2, 'Temporada 2'), (3, 'Temporada 3'), (4, 'Temporada 4'), (5, 'Temporada 5'), (6, 'Temporada 6'), (7, 'Temporada 7'), (8, 'Temporada 8'), (9, 'Temporada 9'), (10, 'Temporada 10')]),
        ),
    ]