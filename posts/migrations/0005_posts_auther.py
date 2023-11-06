# Generated by Django 4.2 on 2023-11-06 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='auther',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_auther', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
