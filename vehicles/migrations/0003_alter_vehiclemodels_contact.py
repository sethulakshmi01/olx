# Generated by Django 4.1.4 on 2023-09-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehiclemodels_delete_vehicles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodels',
            name='contact',
            field=models.CharField(max_length=15),
        ),
    ]
