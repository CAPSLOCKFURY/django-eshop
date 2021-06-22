"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.urls import path
from .views import ProductViewSet, product_detail

urlpatterns = [
    path('<int:pk>', ProductViewSet.as_view({'get': 'list'})),
    path('product-detail/<int:pk>/', product_detail)
]