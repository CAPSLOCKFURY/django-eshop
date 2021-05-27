from django.db import models
from order.models import Order


class Cart(models.Model):
    product_id = models.ForeignKey('main.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart_id = models.CharField(max_length=255)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.product_id}|{self.quantity}|{self.cart_id}'

