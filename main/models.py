from django.db import models
from datetime import datetime
from django.utils.timezone import now
from cart.models import Cart


class Product(models.Model):
    title = models.CharField('Title', max_length=516)
    description = models.TextField('Description', blank=True)
    date = models.DateTimeField('Date', default=now, blank=True)
    price = models.DecimalField('Price', decimal_places=1, max_digits=10000)
    category = models.ForeignKey('main.Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def add_to_cart(self, cartid):
        cart = Cart(cart_id=cartid, quantity=1, product_id_id=self.id)
        cart.save()

    def remove_from_cart(self, cartid):
        cart_product = Cart.objects.get(cart_id=cartid, product_id_id=self.id, order_id=0)
        cart_product.delete()

    def plus_quantity(self, cartid):
        cart_product = Cart.objects.get(cart_id=cartid, product_id_id=self.id, order_id=0)
        cart_product.quantity += 1
        cart_product.save()

    def minus_quantity(self, cartid):
        cart_product = Cart.objects.get(cart_id=cartid, product_id_id=self.id, order_id=0)
        cart_product.quantity -= 1
        if cart_product.quantity == 0:
            cart_product.delete()
        else:
            cart_product.save()

    def get_absolute_url(self):
        return f'/product/{self.id}'


class Category(models.Model):
    name = models.CharField('Category', max_length=512)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return f'/category/{self.id}'
