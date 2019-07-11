# Generated by Django 2.2.3 on 2019-07-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0004_auto_20190709_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='produccion',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='videos',
            name='categoria',
        ),
        migrations.AddField(
            model_name='videos',
            name='categoria',
            field=models.ManyToManyField(to='videoteca.Categorias'),
        ),
    ]
