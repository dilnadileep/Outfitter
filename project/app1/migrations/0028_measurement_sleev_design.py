# Generated by Django 4.2.5 on 2023-11-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_alter_measurement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sleev_design',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
