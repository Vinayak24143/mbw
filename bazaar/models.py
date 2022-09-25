from django.db import models
from defaultPickers.models import Country, State,District,City
def bazaarImage(instance, filename):
    return '/'.join( ['bazaar', str(instance.id), filename] )


def productImage(instance, filename):
    return '/'.join( ['product', str(instance.id), filename] )

def bazaarGroupImage(instance, filename):
    return '/'.join( ['bazaargroup', str(instance.id), filename] )

def productCategoryImage(instance, filename):
    return '/'.join( ['prductcategory', str(instance.id), filename] )

def productSubCategoryImage(instance, filename):
    return '/'.join( ['prductsubcategory', str(instance.id), filename] )


class Group(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=bazaarGroupImage,
        max_length=254, blank=True, null=True
    )
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True, blank=True)
    gst = models.IntegerField(null=True)
    hsnCode = models.CharField(max_length=100, null=True)

    frontImage = models.ImageField(
        upload_to=productImage,
        max_length=254, blank=True, null=True
    )
    backImage = models.ImageField(
        upload_to=productImage,
        max_length=254, blank=True, null=True
    )
    mrpImage = models.ImageField(
        upload_to=productImage,
        max_length=254, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=productCategoryImage,
        max_length=254, blank=True, null=True
    )
    def __str__(self) -> str:
        return self.name

class ProductSubCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=productSubCategoryImage,
        max_length=254, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name

class Bazaar(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, null=True,on_delete=models.SET_NULL)
    dist = models.ManyToManyField(District)
    city = models.ManyToManyField(City)
    group = models.ManyToManyField(Group)
    productCategory = models.ManyToManyField(ProductCategory)
    productSubCategory = models.ManyToManyField(ProductSubCategory)
    product = models.ManyToManyField(Product)
    image = models.ImageField(
        upload_to=bazaarImage,
        max_length=254, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name
    