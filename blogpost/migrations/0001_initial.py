# Generated by Django 3.2.19 on 2023-05-31 18:36

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stripdetail', '0003_auto_20230530_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('content', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spost', to=settings.AUTH_USER_MODEL)),
                ('strip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strip', to='stripdetail.stripdetail')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
