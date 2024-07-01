from django.shortcuts import render, redirect

from shop.forms import CommentForm
from shop.models import Product, Comment


# Create your views here.


def product_list(request):
    searched = request.GET.get('searched')
    if searched:
        products_list = Product.objects.filter(name__icontains=searched)
    else:
        products_list = Product.objects.all()

    context = {'products_list': products_list}


    return render(request, 'shop/home.html', context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    comments = Comment.objects.filter(product=product_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
            return redirect('detail', product_id=product.id)
    else:
        comment_form = CommentForm()

    context = {
        'product': product,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'shop/detail.html', context)