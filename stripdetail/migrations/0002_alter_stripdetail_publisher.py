# Generated by Django 3.2.19 on 2023-05-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripdetail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripdetail',
            name='publisher',
            field=models.CharField(max_length=100),
        ),
    ]
