"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.db import models
from main.models import Product


class SpecificationPreset(models.Model):
    name = models.CharField(max_length=516)
    category = models.ForeignKey('main.Category', on_delete=models.CASCADE, null=True, related_name='cat_specs')
    is_filter = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.category}|{self.name}'


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='specifications')
    name = models.ForeignKey(SpecificationPreset, on_delete=models.CASCADE, related_name='specs_name')
    specification = models.CharField(max_length=516)

    def __str__(self):
        return f'{self.name}|{self.specification}'
