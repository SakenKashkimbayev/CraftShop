from django.contrib import admin
from django.urls import path

from shop.views import new_product, CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    # path('', index),
    path('', CategoryListView.as_view()),
    path('new/', new_product),
    path('<int:category_id>/', ProductListView.as_view()),
    path('<int:category_id>/<int:pk>/', ProductDetailView.as_view()),
]
