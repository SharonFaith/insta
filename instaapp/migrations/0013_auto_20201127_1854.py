# Generated by Django 3.1.3 on 2020-11-27 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaapp', '0012_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='pic_image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='numlikes', to='instaapp.image'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
