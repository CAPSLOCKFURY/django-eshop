"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.db import models
from django.utils.timezone import now
from cart.models import Cart
from django.urls import reverse


class Product(models.Model):
    title = models.CharField('Title', max_length=516)
    description = models.TextField('Description', blank=True, help_text='This field is optional')
    date = models.DateTimeField('Date', default=now, blank=True)
    price = models.DecimalField('Price', decimal_places=1, max_digits=10000, help_text='Price in usd')
    category = models.ForeignKey('main.Category', on_delete=models.CASCADE, null=True)
    posted = models.BooleanField(default=True, help_text='Is checked it will show up at the shop')

    def __str__(self):
        return self.title

    def plus_quantity(self, cartid):
        cart_product = Cart.objects.get(cart_id=cartid, product_id_id=self.id, order_id__isnull=True)
        cart_product.quantity += 1
        cart_product.save()

    def minus_quantity(self, cartid):
        cart_product = Cart.objects.get(cart_id=cartid, product_id_id=self.id, order_id__isnull=True)
        cart_product.quantity -= 1
        if cart_product.quantity == 0:
            cart_product.delete()
        else:
            cart_product.save()

    def remove_from_cart(self, cartid):
        cart_product = Cart.objects.get(cart_id=cartid, product_id_id=self.id, order_id__isnull=True)
        cart_product.delete()

    def add_to_cart(self, cartid):
        product_exists = Cart.objects.filter(product_id_id=self.id, cart_id=cartid, order_id__isnull=True)
        if not product_exists:
            cart = Cart(cart_id=cartid, quantity=1, product_id_id=self.id)
            cart.save()
        else:
            self.plus_quantity(cartid)

    def get_absolute_url(self):
        return reverse('product', kwargs={"id": self.id})


class Category(models.Model):
    name = models.CharField('Category', max_length=512)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('category-products', kwargs={'category': self.id})

    def get_specs_absolute_url(self):
        return reverse('specifications', kwargs={"id": self.id})
