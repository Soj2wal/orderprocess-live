from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True,  null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Electronic Accessories', 'Electronic Accessories'),
        ('Mobile & Tablet Accessories', 'Mobile & Tablet Accessories'),
        ('TV & Home Appliances', 'TV & Home Appliances'),
        ('Kitchenware & Dinning ', 'Kitchenware & Dinning'),

    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,  null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,  null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name


class Staff(models.Model):
    POSITION = (
        ('Manager', 'Manager'),
        ('Hr', 'Hr'),
        ('Sales', 'Sales'),
        ('Cleaner', 'Cleaner')
    )
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, null=True)
    increment_rate = models.FloatField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,  null=True)
    position = models.CharField(
        max_length=200, null=True, choices=POSITION, blank=True)
    profile_pic = models.ImageField(
        default="profile.jpg", null=True, blank=True)

    def __str__(self):
        return self.name
