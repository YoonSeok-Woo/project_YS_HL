# Generated by Django 3.2.9 on 2021-11-18 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_community_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='community',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='community.community'),
            preserve_default=False,
        ),
    ]
