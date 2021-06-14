"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.contrib import admin
from .models import Product, Category
from cart.models import Cart
from order.models import Order
from specifications.models import Specification, SpecificationPreset
from django.urls import resolve
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class SpecificationInline(admin.TabularInline):
    model = Specification

    def get_parent(self, request):
        resolved = resolve(request.path_info)
        if resolved.kwargs.get('object_id'):
            return self.parent_model.objects.get(pk=resolved.kwargs['object_id'])
        return None

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        parent = self.get_parent(request)
        if parent is None:
            if db_field.name == "name":
                kwargs["queryset"] = SpecificationPreset.objects.order_by('category')
        else:
            if db_field.name == "name":
                kwargs["queryset"] = SpecificationPreset.objects.filter(category_id=parent.category_id)
        return super(SpecificationInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class ProductAdmin(admin.ModelAdmin):
    inlines = [SpecificationInline]
    list_display = ['title', 'price', 'category']
    list_filter = ['category', 'posted']
    search_fields = ['title']
    fieldsets = (
        ('Main', {'fields': ('title', 'category', 'price', 'description')}),
        ('Meta', {'fields': ('date', 'posted')}),
    )

    class Meta:
        model = Product


class OrderInlines(admin.TabularInline):
    model = Cart
    exclude = ['cart_id']
    readonly_fields = ['product_id', 'quantity']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInlines]
    list_display = ['order_date', 'delivery_type']
    list_filter = ['order_date','delivery_type']
    exclude = ['user_id', 'order_id']
    readonly_fields = ['delivery_type', 'comment']

    class Meta:
        model = Order


class CategoryInline(admin.TabularInline):
    model = SpecificationPreset
    verbose_name_plural = 'Specification Names'


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    search_fields = ['name']

    class Meta:
        model = Category


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.unregister(User)
admin.site.unregister(Group)
#admin.site.register(Specification)
#admin.site.register(Cart)
#admin.site.register(SpecificationPreset)
