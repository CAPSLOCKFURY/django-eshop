from functools import wraps
from django.shortcuts import redirect
from eshop.settings import CART_ID_REDIRECT


def cart_id_required(f):
    @wraps(f)
    def wrapper(requst, *args, **kwargs):
        if 'cart_id' in requst.session:
            return f(requst, *args, **kwargs)
        else:
            return redirect(CART_ID_REDIRECT)

    return wrapper
