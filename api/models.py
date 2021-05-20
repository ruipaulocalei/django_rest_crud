from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(blank=True, null=True, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    countInStock = models.IntegerField(default=0)