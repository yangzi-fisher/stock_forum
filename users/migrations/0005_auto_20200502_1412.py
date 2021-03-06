# Generated by Django 3.0.4 on 2020-05-02 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
        ('users', '0004_auto_20200502_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='following_stock',
        ),
        migrations.AddField(
            model_name='followingstocks',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='following_plate',
            field=models.ManyToManyField(to='forum.Plate'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='following_post',
            field=models.ManyToManyField(to='forum.Post'),
        ),
    ]
