"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from filters.models import Filter
from django.core.paginator import Paginator, EmptyPage
from eshop.funcs import cart_id_get_or_create, get_url_kwargs


def main_view(request, category):
    products = Filter().get_filtered_products(request, category)

    if request.method == "GET":
        q = request.GET.get("q", "")
        products = products.filter(title__icontains=q)
        q_filter = Filter().get_specs_filters(request)
        for filter in q_filter:
            products = products.filter(**filter)
            if products:
                continue
            else:
                break

    p = Paginator(products, request.session.get('objs_on_page', 5))

    try:
        products = p.page(request.GET.get('page', 1))
    except EmptyPage:
        return redirect('/category/{}?{}'.format(category, get_url_kwargs(request)))

    ctx = {'products': products, 'paginator': p, 'category_id': category}
    return render(request, 'index.html', ctx)


def category_view(request):
    categories = Category.objects.all()
    return render(request, 'all-categories.html', {'categories': categories})


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


def category_specs(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'specifications.html', {'category': category})


def test_api(request):
    return render(request, 'test-api.html')
