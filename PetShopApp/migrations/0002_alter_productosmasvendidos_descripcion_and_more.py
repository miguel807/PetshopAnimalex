# Generated by Django 4.1.2 on 2023-01-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetShopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosmasvendidos',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='productosofertas',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='productosperrosgatos',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]