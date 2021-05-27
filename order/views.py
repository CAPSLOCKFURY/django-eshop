from django.shortcuts import render, redirect
from .models import Order
from django.contrib.auth.decorators import login_required
from eshop.decorators import cart_id_required
from .forms import OrderForm
from eshop.funcs import cart_id_get_or_create


@login_required
def all_orders(request):
    orders = Order.objects.all().order_by('-id')
    return render(request, 'admin/orders.html', {'orders': orders})


@cart_id_required
def order_details(request, id):
    orders = Order.objects.get(order_id=id)
    ctx = {'orders': orders}
    return render(request, 'order-details.html', ctx)


@cart_id_required
def order_product(request):

    if request.method == "POST":
        order = OrderForm(request.POST)
        if order.is_valid():
            order = order.save(commit=False)
            order.make_order(request.session['cart_id'])
            return redirect(order.get_absolute_url())

    form = OrderForm()
    return render(request, 'order-product.html', {'form': form})


def order_history(request):
    orders = Order.objects.filter(user_id=cart_id_get_or_create(request)).order_by('-id')
    ctx = {'orders': orders}
    return render(request, 'admin/orders.html', ctx)
