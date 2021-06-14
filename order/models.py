"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.db import models
import uuid
from cart.models import Cart


class Order(models.Model):
    DELIVERY_CHOISES = [
        ('', 'other'),
        ('pk', 'pickup'),
        ('dl', 'delivery')
    ]

    user_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_type = models.CharField(choices=DELIVERY_CHOISES, max_length=1000)
    comment = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return str(self.order_date)

    def make_order(self, cart_id):
        order_id = uuid.uuid4().hex
        self.user_id = cart_id
        self.order_id = order_id
        self.save()
        user_cart = Cart.objects.filter(cart_id=cart_id, order_id__isnull=True)
        user_cart.update(order_id=self)

    def get_absolute_url(self):
        return f'/order-details/{self.order_id}'
