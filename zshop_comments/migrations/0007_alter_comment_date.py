# Generated by Django 3.2.4 on 2021-10-16 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zshop_comments', '0006_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
