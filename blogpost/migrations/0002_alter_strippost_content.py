# Generated by Django 3.2.19 on 2023-06-05 20:18

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strippost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
