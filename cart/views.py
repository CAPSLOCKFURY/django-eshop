from django.shortcuts import render, redirect
from cart.models import Cart
from main.models import Product
from eshop.decorators import cart_id_required


def cart_view(request):
    if 'cart_id' in request.session:
        user_cart = Cart.objects.filter(cart_id=request.session['cart_id'], order_id="0")
        ctx = {'cart': user_cart}
    else:
        ctx = {'empty': 'Your cart is empty'}
    return render(request, 'cart.html', ctx)


@cart_id_required
def cart_delete(request, id):
    product = Product.objects.get(id=id)
    product.remove_from_cart(request.session['cart_id'])
    return redirect('cart')


@cart_id_required
def cart_quantity(request, id, action):
    product = Product.objects.get(id=id)
    if action == "+":
        product.plus_quantity(request.session['cart_id'])
    elif action == "-":
        product.minus_quantity(request.session['cart_id'])
    else:
        return redirect('cart')
    return redirect('cart')


