# Generated by Django 5.0.6 on 2024-07-05 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
