from django.contrib import admin
from django.urls import path

from shop import views
from shop.views import CategoryListView, ProductListView, ProductDetailView, NewProduct

urlpatterns = [
    # path('', index),
    path('', CategoryListView.as_view(), name='index'),
    path('new/', NewProduct.as_view()),
    path('test/', views.test_view),
    path('<int:category_id>/', ProductListView.as_view()),
    path('<int:category_id>/<int:pk>/', ProductDetailView.as_view()),
]
