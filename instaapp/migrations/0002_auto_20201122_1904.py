# Generated by Django 3.1.3 on 2020-11-22 16:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None), size=None),
        ),
    ]