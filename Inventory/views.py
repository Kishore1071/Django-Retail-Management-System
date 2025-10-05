from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import *
from .forms import *


class CategoryList(LoginRequiredMixin, ListView):

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryCreate(LoginRequiredMixin, CreateView):

    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Create"
        context['button_name'] = "Add"

        return context

class CategoryUpdate(LoginRequiredMixin, UpdateView):

    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update"
        context['button_name'] = "Update"

        return context

class CategoryDelete(LoginRequiredMixin, DeleteView):

    model = Category
    template_name = 'category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')


class ProductsList(LoginRequiredMixin, View):

    def get(self, request):

        context = {
            "all_products": Product.objects.all()
        }

        return render(request, 'products_list.html', context)
    
class ProductsCreate(LoginRequiredMixin, View):

    def get(self, request):

        context = {
            'form': ProductForm(),
            'title': 'Create',
            'button_name': 'Add'
        }

        return render(request, 'product_create.html', context)

    def post(self, request):

        product_form = ProductForm(request.POST)

        if product_form.is_valid():

            product_form.save()

            return redirect('/inventory/products/list/')

class ProductUpdate(LoginRequiredMixin, View):

    def get(self, request, id):

        selected_product = Product.objects.get(id = id)

        context = {
            "form" : ProductForm(instance=selected_product),
            'title': 'Update',
            'button_name': 'Update'
        }

        return render(request, 'product_create.html', context)

    def post(self, request, id):

        selected_product = Product.objects.get(id = id)

        product_form = ProductForm(request.POST, instance=selected_product)

        if product_form.is_valid():

            product_form.save()

            return redirect('/inventory/products/list/')
    
class ProductDelete(LoginRequiredMixin, View):

    def get(self, request, id):

        selected_product = Product.objects.get(id = id)

        selected_product.delete()

        return redirect('/inventory/products/list/')


@login_required(login_url='/inventory/products/list/')
def stock_list(request):

    all_products = Product.objects.all()

    product_collection = []
    for product in all_products:

        product.low_stock = product.quantity <= product.minimum_quantity

        product_collection.append(product)

    print(product_collection)

    context = {
        "products": product_collection
    }

    return render(request, 'stock_list.html', context)

@login_required(login_url='/inventory/products/list/')
def stock_update(request, id):

    selected_product = Product.objects.get(id=id)

    product_data = Product.objects.filter(id=id)

    product_data.update(quantity=float(selected_product.quantity) + float(request.POST['quantity']))

    return redirect('/inventory/stock/list/')





