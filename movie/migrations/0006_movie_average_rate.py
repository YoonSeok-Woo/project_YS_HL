# Generated by Django 3.2.9 on 2021-11-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_movie_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='average_rate',
            field=models.FloatField(blank=True, default=0),
        ),
    ]