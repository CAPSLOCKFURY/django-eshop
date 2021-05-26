from django.contrib import admin
from django.urls import path
from main import views as main_views
from cart import views as cart_views
from order import views as order_views
from filters import views as filter_views


urlpatterns = [
    # админские урлы
    path('admin/', admin.site.urls),
    path('admin/add-product', main_views.add_product, name='add'),
    path('admin/orders', order_views.all_orders, name='all-orders'),
    path('admin/add-category', main_views.add_category, name='add-category'),
    path('admin/delete-product/<int:id>', main_views.delete_product, name='delete-product'),
    path('admin/delete-category/<int:id>', main_views.delete_category, name='delete-cat'),
    path('session/', main_views.session_test),
    # основные урлы
    path('', main_views.main_view, name='main'),
    path('product/<int:id>', main_views.product_detail, name='product'),
    path('filters/', filter_views.save_filter, name='filter'),
    path('category/<str:cat>', main_views.category_view, name='category'),
    path('order-history/', order_views.order_history, name='order_history'),
    # урлы корзины
    path('cart/', cart_views.cart_view, name='cart'),
    path('cart-delete/<int:id>', cart_views.cart_delete, name='cart-delete'),
    path('cart-quantity-manager/<int:id>/<str:action>', cart_views.cart_quantity, name='quantity'),
    # урлы заказов
    path('order-product/', order_views.order_product, name='make-order'),
    path('order-details/<str:id>', order_views.order_details, name='order-details'),
]
