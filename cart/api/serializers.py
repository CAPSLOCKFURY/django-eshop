"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from rest_framework import serializers
from ..models import Cart
from main.api.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = Cart
        fields = ['quantity', 'product_id']
