# Generated by Django 5.2 on 2025-04-30 14:26

import django.utils.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(verbose_name=django.utils.text.slugify),
        ),
    ]
