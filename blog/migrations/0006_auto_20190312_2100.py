# Generated by Django 2.1.5 on 2019-03-12 21:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(limit_value=2)]),
        ),
    ]
