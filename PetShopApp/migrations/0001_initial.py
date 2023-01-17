# Generated by Django 4.1.2 on 2023-01-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductosMasVendidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=10)),
                ('imagen', models.ImageField(upload_to='Fotos')),
            ],
            options={
                'verbose_name': 'ProductoMasVendidos',
            },
        ),
        migrations.CreateModel(
            name='ProductosOfertas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=10)),
                ('imagen', models.ImageField(upload_to='Fotos')),
            ],
            options={
                'verbose_name': 'ProductosOfertas',
            },
        ),
        migrations.CreateModel(
            name='ProductosPerrosGatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=10)),
                ('imagen', models.ImageField(upload_to='Fotos')),
            ],
            options={
                'verbose_name': 'ProductosPerrosGatos',
            },
        ),
    ]
