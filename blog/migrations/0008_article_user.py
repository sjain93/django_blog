# Generated by Django 2.1.5 on 2019-03-17 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20190312_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='poster', to=settings.AUTH_USER_MODEL),
        ),
    ]
