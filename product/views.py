from django.shortcuts import render
from product.models import Product


def products(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})
