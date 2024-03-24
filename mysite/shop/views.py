from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from shop.forms import AddProductForms
from shop.models import Category, Product


def index(request):
    c = Category.objects.all()
    context = {
        'category': c
    }
    return HttpResponse(render(request, 'shop/index.html', context))

def category(request, category_id):
    c = Category.objects.get(id=category_id)
    p = Product.objects.filter(category_id=c.id)
    context = {
        'category': c,
        'product': p
    }
    return HttpResponse(render(request, 'shop/category.html', context))

def new_product(request):
    if request.method == 'POST':
        form = AddProductForms(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            return HttpResponse('ErrorCreating')
    context = {
        'form':AddProductForms()
    }
    return render(request, 'shop/new_product.html', context=context)




















# def index(request):
#     c = Category.objects.all()
#     # response = (
#     #     f'<ul>'
#     #     f"{ ''.join([f'<li>{c1.name}</li>' for c1 in c])}"
#     #     f'</ul>'
#     #
#     # )
#     # return HttpResponse('<h1>Добро пожаловать в наш магазин</h1>'
#     #                     f'В нашем магазине есть следующие категорий товаров: {response}')
#
#     # template = loader.get_template('shop/index.html')
#     context = {
#         'category': c
#     }
#     # return HttpResponse(template.render(context, request))
#     return HttpResponse(render(request, 'shop/index.html', context))
#
# # def category(request):
# #     category_id = request.GET.get('id', 1)
# #     c = Category.objects.get(id=category_id)
# #     return HttpResponse(f'<h1> id: {c.id}. {c.name} </h1>'
# #                         f'<p> {c.description} </p>')
# def category(request, category_id):
#     c = Category.objects.get(id=category_id)
#     p = Product.objects.filter(category_id=c.id)
#     response = (
#         f'<ul>'
#         f"{''.join([f'<li>{p1.name}</li>' for p1 in p])}"
#         f'</ul>'
#
#     )
#     return HttpResponse(f'<h1> В категории {c.name} есть товары:</h1>'
#                         f'{response}')