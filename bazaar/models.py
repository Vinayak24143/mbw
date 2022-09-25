from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class ProductSubCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Bazaar(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    dist = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    group = models.ManyToManyField(Group)
    productCategory = models.ManyToManyField(ProductCategory)
    productSubCategory = models.ManyToManyField(ProductSubCategory)
    product = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.name