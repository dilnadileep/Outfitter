# Generated by Django 4.2.5 on 2023-11-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_measurement_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='lining_design',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
