from django import forms
from .models import Product, Bill, BillItem


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['customer_name']

class BillItemForm(forms.ModelForm):
    class Meta:
        model = BillItem
        fields = ['product', 'quantity']
