from django.urls import path
from .views import *

urlpatterns = [
    path('category/list/', CategoryList.as_view(), name='category_list'),
    path('category/create/', CategoryCreate.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),

    path('products/list/', ProductsList.as_view(), name='product_list'),
    path('product/create/', ProductsCreate.as_view(), name='product_create'),
    path('product/update/<int:id>/', ProductUpdate.as_view(), name='product_update'),
    path('product/delete/<int:id>/', ProductDelete.as_view(), name='product_delete'),

    path('stock/list/', stock_list, name='stock_list'),
    path('stock/update/<int:id>/', stock_update, name='stock_update'),
]