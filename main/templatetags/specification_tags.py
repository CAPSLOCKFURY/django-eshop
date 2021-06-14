"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django import template
from specifications.models import Specification

register = template.Library()


@register.simple_tag
def get_specifications(name, cat):
    specs = Specification.objects.filter(name__name=name, name__category__name=cat).values('specification').distinct()
    return specs


@register.simple_tag(takes_context=True)
def get_specifications_from_get_params(context):
    keys = []
    link = ['']
    request = context['request'].GET.copy()
    for key in request:
        if key != 'page':
            keys.append(key)
    for key in keys:
        values = request.getlist(f'{key}')
        for value in values:
            link.append(f'&{key}={value}')

    return ''.join(link)


@register.simple_tag(takes_context=True)
def get_specs_dictionary(context):
    res = {}
    request = context['request'].GET.copy()
    for key in request:
        if key != 'page' and key != 'q':
            res[f'{key}'] = request.getlist(f'{key}')

    return res


@register.simple_tag()
def check_if_checked(key, value, dict):
    if value in dict[f'{key}']:
        return True
    else:
        return False

