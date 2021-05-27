from django.db import models
from main.models import Product


class SpecificationPreset(models.Model):
    name = models.CharField(max_length=516)

    def __str__(self):
        return self.name


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.ForeignKey(SpecificationPreset, on_delete=models.CASCADE)
    specification = models.CharField(max_length=516)

    def __str__(self):
        return f'{self.name}|{self.specification}'
