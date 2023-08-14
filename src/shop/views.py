from django.shortcuts import render
from .models import Product


def all_products_by_category(request, category=None):
    data = {
        'products': []
    }
    for product in Product.objects.all():
        if category == None or category == product.category:
            data['products'].append(product)
    return render(request, 'shop/products.html', context=data)


def delivery(request):
    return render(request, 'shop/delivery.html')


def all_products(request):
    data = {
        'products': []
    }
    for product in Product.objects.all():
        data['products'].append(product)
    return render(request, 'shop/products.html', context=data)


def sale_products(request):
    data = {
        'sale_products': []
    }
    for product in Product.objects.all():
        if product.old_price != None:
            data['sale_products'].append(product)
    return render(request, 'shop/sale.html', context=data)


def main_page(request):
    data = {
        'popular_products': Product.objects.filter(popular=True)
    }
    return render(request, 'shop/main_page.html', context=data)


def menu(request):
    data = {}
    return render(request, 'shop/menu.html', context=data)
