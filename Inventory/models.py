from django.db import models


class Category(models.Model):

    category_name = models.CharField(max_length=200)

    def __str__(self):

        return self.category_name
    

class Product(models.Model):

    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    minimum_quantity = models.FloatField(default=0)

    def __str__(self):

        return self.product_name
