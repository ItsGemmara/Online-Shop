from django.db import models
from User.models import Customer
from Media.models import Image, Video, Comment
from Salesman.models import Salesman


class Category(models.Model):
    pass


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    sub_category = models.ManyToManyField(SubCategory)
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class ProductImage(Image):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductVideo(Video):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductComment(Comment):
    product = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Description(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
