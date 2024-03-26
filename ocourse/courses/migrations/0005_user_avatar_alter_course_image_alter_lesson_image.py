# Generated by Django 5.0.3 on 2024-03-25 14:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_tag_lesson_comment_course_tags_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]
