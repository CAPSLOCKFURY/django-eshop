"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

import uuid


def cart_id_get_or_create(request):
    if 'cart_id' not in request.session:
        request.session['cart_id'] = uuid.uuid1().hex
        cart_id = request.session['cart_id']
    else:
        cart_id = request.session['cart_id']
    return cart_id


def get_url_kwargs(request):
    keys = []
    link = ['']
    request = request.GET.copy()

    for key in request:
        if key != 'page':
            keys.append(key)

    for key in keys:
        values = request.getlist(f'{key}')
        for value in values:
            link.append(f'&{key}={value}')

    return ''.join(link)
