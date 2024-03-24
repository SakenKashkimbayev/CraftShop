from django.contrib import admin
from django.urls import path

from shop.views import index, category, new_product

urlpatterns = [
    path('', index),
    path('new/', new_product),
    path('<int:category_id>/', category),
]
