# Generated by Django 4.2.5 on 2023-10-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_product_delivery_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
