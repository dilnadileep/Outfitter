# Generated by Django 4.2.5 on 2023-11-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_product_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bust', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('waist', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hips', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('shoulder_width', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sleeve_length', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
