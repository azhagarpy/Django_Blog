# Generated by Django 4.1.7 on 2023-03-18 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_rename_category_blog_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='category_id',
        ),
    ]
