from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

class ProductSubCategory(models.Model):
    name = models.CharField(max_length=255)

class Bazaar(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    dist = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    group = models.ManyToManyField(Group)
    productCategory = models.ManyToManyField(ProductCategory)
    productSubCategory = models.ManyToManyField(ProductSubCategory)
    product = models.ManyToManyField(Product)