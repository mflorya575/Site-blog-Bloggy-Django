# Generated by Django 4.2.1 on 2024-02-19 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_post_create_post_status_post_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create',
        ),
        migrations.RemoveField(
            model_name='post',
            name='update',
        ),
    ]
