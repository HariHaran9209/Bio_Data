# Generated by Django 4.2.19 on 2025-02-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0002_customusermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
