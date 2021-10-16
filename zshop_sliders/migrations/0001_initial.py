# Generated by Django 3.2.3 on 2021-06-05 07:12

from django.db import migrations, models
import zshop_sliders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('link', models.URLField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=zshop_sliders.models.upload_image_path)),
            ],
        ),
    ]
