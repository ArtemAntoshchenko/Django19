from django.db import models

class Product(models.Model):
    name=models.CharField()

class Store(models.Model):
    name=models.CharField()
    products=models.ManyToManyField(Product, through='Metadata')

class Metadata(models.Model):
    store=models.ForeignKey(Store, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10000,decimal_places=2)