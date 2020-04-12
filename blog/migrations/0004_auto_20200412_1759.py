# Generated by Django 2.2.12 on 2020-04-12 12:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20200412_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikers',
            field=models.ManyToManyField(related_name='dislikers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likers',
            field=models.ManyToManyField(related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]
