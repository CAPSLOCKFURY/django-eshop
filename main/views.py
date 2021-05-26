from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Category
from .forms import ProductAddForm
from cart.models import Cart
import uuid
from django.contrib.auth.decorators import login_required
from eshop.decorators import cart_id_required
from eshop.settings import ORDER_FILTER
from filters.models import Filter
from django.core.paginator import Paginator, EmptyPage


def main_view(request):
    products = Product.objects.all().order_by(ORDER_FILTER[request.session.get('filter_by', '0')])
    f = Filter(min_price=request.session.get('min_price', 0), max_price=request.session.get('max_price', 0), category_id=request.session.get('category', 0))
    f.make_filter()
    f = f.get_filter()
    if f:
        products = products.filter(**f)
    if request.method == "GET":
        q = request.GET.get("q")
        if q:
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
        if 'cart_id' not in request.session:
            request.session['cart_id'] = uuid.uuid1().hex
            cart_id = request.session['cart_id']
        else:
            cart_id = request.session['cart_id']

        product_exists = Cart.objects.filter(product_id_id=id, cart_id=cart_id, order_id=0)
        if not product_exists:
            product.add_to_cart(cart_id)
        else:
            product.plus_quantity(cart_id)

    ctx = {'product': product}
    return render(request, 'product-details.html', ctx)


@cart_id_required
def session_test(request):
    return HttpResponse('<h1>{}</h1>'.format(request.session['cart_id']))


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductAddForm(request.POST)
        if form.is_valid():
            prod = form.save()
            return redirect(f'/product/{prod.id}')
    form = ProductAddForm()
    return render(request, 'admin/add-product.html', {"form": form})


@login_required
def add_category(request):
    if request.method == "POST":
        if request.POST['cat-name']:
            cat = Category(name=request.POST['cat-name'])
            cat.save()
    return render(request, 'admin/add-category.html')


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

