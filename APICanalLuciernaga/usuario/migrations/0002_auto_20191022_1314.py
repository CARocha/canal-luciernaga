# Generated by Django 2.2.3 on 2019-10-22 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email', 'username')},
        ),
    ]
