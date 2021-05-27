import uuid


def cart_id_get_or_create(request):
    if 'cart_id' not in request.session:
        request.session['cart_id'] = uuid.uuid1().hex
        cart_id = request.session['cart_id']
    else:
        cart_id = request.session['cart_id']
    return cart_id
