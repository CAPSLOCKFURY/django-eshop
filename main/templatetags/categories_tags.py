"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()
