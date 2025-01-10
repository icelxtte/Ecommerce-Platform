from django.db import models
import datetime
import os

# Ensure `os` is imported only in `settings.py`, not in `models.py`
# import os  # This should be in settings.py, not here

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name

# All of product's attributes are defined here
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)  # Corrected field definition
    description = models.TextField(max_length=1000, default='', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

# Customer's order is defined here
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
