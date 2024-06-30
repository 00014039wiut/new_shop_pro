from django.shortcuts import render

from shop.models import Product


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/home.html', context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)
