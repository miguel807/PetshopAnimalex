from django.db import models

# Create your models here.
class ProductosMasVendidos(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100,blank=True)
    precio = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='Fotos')
    class Meta:
        verbose_name = 'ProductoMasVendidos'
    def __str__(self):
        return self.nombreProducto


class ProductosOfertas(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100,blank=True)
    precio = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='Fotos')
    class Meta:
        verbose_name = 'ProductosOfertas'

    def __str__(self):
        return self.nombreProducto


class ProductosPerrosGatos(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100,blank=True)
    precio = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='Fotos')

    class Meta:
        verbose_name = 'ProductosPerrosGatos'

    def __str__(self):
        return self.nombreProducto


class ProductosPeces(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100,blank=True)
    precio = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='Fotos')

    class Meta:
        verbose_name = 'ProductosPeces'

    def __str__(self):
        return self.nombreProducto

class ProductosAves(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100,blank=True)
    precio = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='Fotos')

    class Meta:
        verbose_name = 'ProductosAves'

    def __str__(self):
        return self.nombreProducto


class ProductosHansterArdillas(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100,blank=True)
    precio = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='Fotos')

    class Meta:
        verbose_name = 'ProductosHansterArdillas'

    def __str__(self):
        return self.nombreProducto
