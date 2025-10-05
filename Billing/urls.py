from django.urls import path
from .views import *

urlpatterns = [
    path('bills/', bill_list, name='bill_list'),
    path('bills/create/', bill_create, name='bill_create'),
]