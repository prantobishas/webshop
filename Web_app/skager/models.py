from django.db import models
from django.contrib.auth.models import User

# Model for all the products
class Product(models.Model):
    CATEGORIES = [
        ("Auto's", "Auto's"),
        ('Educatief', 'Educatief'),
        ('Knuffels', 'Knuffels'),
        ('Pistolen en geweren', 'Pistolen en geweren'),
        ('Poppen', 'Poppen'),
        ('Bureau-artikelen', 'Bureau-artikelen'),
        ('Schriften', 'Schriften'),
        ('Schrijfgerei', 'Schrijfgerei'),
        ('Postzegels', 'Postzegels'),
    ]
    category = models.CharField(max_length=64,choices=CATEGORIES)
    image = models.ImageField(default='default.png',upload_to='product_pics')
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} - {self.price}"

# Model to get categories of 'Speelgoed'.
class ToysList(models.Model):
    name = models.CharField(max_length=64)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"

# Model to get categories of 'Schoolartikelen'.
class SchoolList(models.Model):
    name = models.CharField(max_length=64)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"

# Model of the added products to the shoppingcart.
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    amount = models.IntegerField(null=True,blank=True)
    price_one = models.DecimalField(max_digits=5,decimal_places=2)
    price_many = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    objects = models.Manager()

    def __str__(self):
            return f"Product: {self.name} - aantal: {self.amount} - prijs: € {self.price_many}"

# Model of the placed orders.
class MyOrders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ManyToManyField(Cart)
    objects = models.Manager()

    def __str__(self):
        return f"{self.user}"

# Model of the address corresponding to the user.
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    street = models.CharField(max_length=64)
    number = models.CharField(max_length=8)
    zipcode = models.CharField(max_length=8)
    city = models.CharField(max_length=64)
    objects = models.Manager()

    def __str__(self):
        return f"{self.user}"


