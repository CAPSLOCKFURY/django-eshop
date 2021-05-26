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

        # if self.min_price is not None and int(self.min_price) > 0:
        #     self.q.update({'price__gte': self.min_price})
        # elif self.min_price is not None and int(self.min_price) is 0:
        #     if 'price__gte' in self.q:
        #         del self.q['price__gte']

        # if self.max_price is not None and int(self.max_price) > 0:
        #     self.q.update({'price__lte': self.max_price})
        # elif int(self.max_price) is 0:
        #     if 'price__lte' in self.q:
        #         del self.q['price__lte']
        #
        # if self.category_id is not None and int(self.category_id) != 0:
        #     self.q.update({'category__id': self.category_id})
        # elif self.category_id is not None and int(self.category_id) == 0:
        #     if 'category__id' in self.q:
        #         del self.q['category__id']


