# Generated by Django 2.1.7 on 2019-03-04 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190304_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='published_date',
        ),
    ]