# Generated by Django 2.2.3 on 2024-07-03 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20191015_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicacion',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugar.Pais'),
        ),
    ]
