# Generated by Django 4.2.5 on 2023-11-05 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_remove_measurement_product_remove_measurement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
    ]