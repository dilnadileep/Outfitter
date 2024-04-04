# Generated by Django 4.2.5 on 2024-04-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0070_cart_customization_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_design',
            name='back_design',
            field=models.ImageField(blank=True, null=True, upload_to='designs/'),
        ),
        migrations.AlterField(
            model_name='cart_design',
            name='lining_design',
            field=models.ImageField(blank=True, null=True, upload_to='designs/'),
        ),
        migrations.AlterField(
            model_name='cart_design',
            name='neck_design',
            field=models.ImageField(blank=True, null=True, upload_to='designs/'),
        ),
        migrations.AlterField(
            model_name='cart_design',
            name='sleev_design',
            field=models.ImageField(blank=True, null=True, upload_to='designs/'),
        ),
    ]
