# Generated by Django 3.0.4 on 2020-05-27 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mockexchange', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='ownedstock',
            name='user_name',
        ),
    ]
