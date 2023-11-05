# Generated by Django 4.2.5 on 2023-11-05 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_measurement_back_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to=settings.AUTH_USER_MODEL),
        ),
    ]
