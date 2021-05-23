from django.db import models


class Cart(models.Model):
    product_id = models.ForeignKey('main.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255, default="0")

    def __str__(self):
        return f'{self.product_id}|{self.quantity}|{self.cart_id}'

