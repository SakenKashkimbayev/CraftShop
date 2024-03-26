from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from shop.forms import AddProductForms
from shop.models import Category, Product

class CategoryListView(ListView):
    model = Category
    template_name = 'shop/index.html'
    context_object_name = 'category'
    # def get(self, request):
    #     c = Category.objects.all()
    #     context = {
    #         'category': c
    #     }
    #     return HttpResponse(render(request, 'shop/index.html', context))


# def index(request):
#     c = Category.objects.all()
#     context = {
#         'category': c
#     }
#     return HttpResponse(render(request, 'shop/index.html', context))

class ProductListView(ListView):
    model = Product
    template_name = 'shop/category.html'
    context_object_name = 'product'

    def get_queryset(self):
        # Получаем значение параметра маршрута 'category_id'
        category_id = self.kwargs.get('category_id')
        # Фильтруем продукты по заданной категории
        queryset = Product.objects.filter(category__id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем значение параметра маршрута 'category_id'
        category_id = self.kwargs.get('category_id')
        # Добавляем объект категории в контекст
        context['category'] = Category.objects.get(id=category_id)
        return context
# def category(request, category_id):
#     c = Category.objects.get(id=category_id)
#     p = Product.objects.filter(category_id=c.id)
#     context = {
#         'category': c,
#         'product': p
#     }
#     return HttpResponse(render(request, 'shop/category.html', context))

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

class NewProduct(CreateView):
    model = Product
    template_name = 'shop/new_product.html'
    success_url = reverse_lazy('index')
    form_class = AddProductForms

def test_view(request):
    return render(request, 'shop/test_view.html')
# def new_product(request):
#     if request.method == 'POST':
#         form = AddProductForms(request.POST)
#
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#         else:
#             return HttpResponse('ErrorCreating')
#     context = {
#         'form':AddProductForms()
#     }
#     return render(request, 'shop/new_product.html', context=context)
