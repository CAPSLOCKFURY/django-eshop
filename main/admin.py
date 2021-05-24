from django.contrib import admin
from .models import Product, Category
from cart.models import Cart
from order.models import Order

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Category)

