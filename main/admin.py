from django.contrib import admin
from .models import Product, Category
from cart.models import Cart
from order.models import Order
from specifications.models import Specification, SpecificationPreset


class SpecificationInline(admin.TabularInline):
    model = Specification


class ProductAdmin(admin.ModelAdmin):
    inlines = [SpecificationInline]

    class Meta:
        model = Product


admin.site.register(Specification)
admin.site.register(SpecificationPreset)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Category)

