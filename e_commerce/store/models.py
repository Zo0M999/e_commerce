from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='product')
    quantity = models.PositiveIntegerField(default=1)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.full_name = f'{self.category} - {self.name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product