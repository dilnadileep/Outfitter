# Generated by Django 4.2.4 on 2024-03-16 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0066_cart_is_customized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_design',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designs', to='app1.cart'),
        ),
    ]
