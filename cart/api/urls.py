"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.urls import path
from .views import CartViewSet

urlpatterns = [
    path('get-cart/', CartViewSet.as_view({'get': 'list'}))
]