"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.db import models
from eshop.settings import ORDER_FILTER
from main.models import Product


class Filter:
    q = {}

    def __init__(self, max_price=None, min_price=None, category_id=None):
        self.max_price = max_price
        self.category_id = category_id
        self.min_price = min_price
        self.filters = {"price__lte": max_price, "price__gte": min_price, "category__id": category_id}

    def make_filter(self):
        for key, value in self.filters.items():
            if value is not None and int(value) > 0:
                self.q.update({f'{key}': value})
            elif value is not None and int(value) == 0:
                if f'{key}' in self.q:
                    del self.q[f'{key}']

    @property
    def get_filter(self):
        return self.q

    @staticmethod
    def get_specs_filters(request):
        specs_keys = []
        q_filter = []

        for key in request.GET:
            if key != 'page' and key != 'q':
                specs_keys.append(key)

        for key in specs_keys:
            values = request.GET.getlist(f'{key}')
            if len(values) > 1:
                q_filter.append({'specifications__name__name': key, 'specifications__specification__in': values})
            elif len(values) == 1:
                q_filter.append({'specifications__name__name': key, 'specifications__specification': values[0]})

        return q_filter

    def get_filtered_products(self, request, category) -> Product:
        products = Product.objects.filter(category_id=category, posted=True).order_by(ORDER_FILTER[request.session.get('filter_by', '0')])
        self.__init__(min_price=request.session.get('min_price', 0), max_price=request.session.get('max_price', 0),
                      category_id=request.session.get('category', 0))
        self.make_filter()
        f = self.get_filter
        if f:
            return products.filter(**f)
        else:
            return products
