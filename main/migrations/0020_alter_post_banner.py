# Generated by Django 5.1.1 on 2025-05-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
    ]
