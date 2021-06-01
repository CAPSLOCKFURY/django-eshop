"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from filters.models import Filter
from django.core.paginator import Paginator, EmptyPage
from eshop.funcs import cart_id_get_or_create


def main_view(request):
    products = Filter().get_filtered_products(request)

    if request.method == "GET":
        q = request.GET.get("q", "")
        products = products.filter(title__icontains=q)

    p = Paginator(products, request.session.get('objs_on_page', 5))

    try:
        products = p.page(request.GET.get('page', 1))
    except EmptyPage:
        return redirect('/?q={}'.format(request.GET.get('q', '')))

    ctx = {'products': products, 'paginator': p}
    return render(request, 'index.html', ctx)


def category_view(request, cat):
    request.session['category'] = cat
    return redirect('main')


def product_detail(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        cart_id = cart_id_get_or_create(request)
        product.add_to_cart(cart_id)

    ctx = {'product': product}
    return render(request, 'product-details.html', ctx)


@login_required
def delete_product(request, id):
    product = Product.objects.filter(id=id)
    product.delete()
    return redirect('main')


@login_required
def delete_category(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    return redirect('main')

