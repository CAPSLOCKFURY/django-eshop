from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Category


def save_filter(request):
    order_by = request.POST['order_by']
    min_price = request.POST['min-price']
    max_price = request.POST['max-price']
    category = request.POST['category']
    request.session['filter_by'] = order_by
    filter_arr = [max_price, min_price, category]
    filter_name_arr = ['max_price', 'min_price', 'category']
    for f, f_name in zip(filter_arr, filter_name_arr):
        if f:
            request.session[f'{f_name}'] = f
        elif (f == 0 or not f) and f_name in request.session:
            del request.session[f'{f_name}']
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

