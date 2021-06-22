"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from rest_framework import serializers
from ..models import Product, Category
from specifications.api.serializers import SpecificationSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    specifications = SpecificationSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'date', 'specifications', 'category']
