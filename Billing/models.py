from django.db import models
from Inventory.models import *

class Bill(models.Model):
    bill_number = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='BillItem')

    def __str__(self):
        return f"Bill #{self.id} - {self.customer_name}"


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
