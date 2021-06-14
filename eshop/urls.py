"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.contrib import admin
from django.urls import path
from main import views as main_views
from cart import views as cart_views
from order import views as order_views
from filters import views as filter_views


urlpatterns = [
    # админские урлы
    path('admin/', admin.site.urls),
    path('admin/orders', order_views.all_orders, name='all-orders'),
    path('admin/delete-product/<int:id>', main_views.delete_product, name='delete-product'),
    path('admin/delete-category/<int:id>', main_views.delete_category, name='delete-cat'),
    # основные урлы
    path('', main_views.category_view, name='main'),
    path('category/<int:category>', main_views.main_view, name='category-products'),
    path('product/<int:id>', main_views.product_detail, name='product'),
    path('filters/', filter_views.save_filter, name='filter'),
    path('order-history/', order_views.order_history, name='order_history'),
    # урлы корзины
    path('cart/', cart_views.cart_view, name='cart'),
    path('cart-delete/<int:id>', cart_views.cart_delete, name='cart-delete'),
    path('cart-quantity-manager/<int:id>/<str:action>', cart_views.cart_quantity, name='quantity'),
    # урлы заказов
    path('order-product/', order_views.order_product, name='make-order'),
    path('order-details/<str:id>', order_views.order_details, name='order-details'),
    # тест урлы
    path('specifications/<int:id>', main_views.category_specs, name='specifications'),
]
