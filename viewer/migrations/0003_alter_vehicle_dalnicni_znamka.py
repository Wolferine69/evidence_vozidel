# Generated by Django 5.1.5 on 2025-02-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_remove_vehicle_km_vymena_oleje_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='dalnicni_znamka',
            field=models.DateField(blank=True, null=True, verbose_name='Platnost dálniční známky'),
        ),
    ]
