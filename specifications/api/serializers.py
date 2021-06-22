"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from rest_framework import serializers
from ..models import Specification, SpecificationPreset
from main.models import Category


class SpecificationSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField('get_spec_name')

    class Meta:
        model = Specification
        exclude = ('product', 'id')

    def get_spec_name(self, obj):
        return obj.name.name


class IsActiveSpecificartion(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(is_filter=True)
        return super().to_representation(data)


class SpecificationNameSerializer(serializers.ModelSerializer):
    specs_name = SpecificationSerializer(many=True)

    class Meta:
        model = SpecificationPreset
        fields = ['id', 'name', 'specs_name']
        list_serializer_class = IsActiveSpecificartion


class CategoryRelatedSpecificationsSerializer(serializers.ModelSerializer):
    cat_specs = SpecificationNameSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'cat_specs']
