from django.db import models
from eshop.settings import ORDER_FILTER


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

    def get_filter(self):
        return self.q


