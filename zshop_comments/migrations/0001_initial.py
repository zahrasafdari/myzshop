# Generated by Django 3.2.4 on 2021-10-15 17:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zshop_products', '0009_product_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(default=datetime.date.today)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zshop_products.product')),
            ],
        ),
    ]
