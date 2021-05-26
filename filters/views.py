from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Category


def save_filter(request):
    request.session['filter_by'] = request.POST['order_by']
    filter_dict = {}
    for key, value in request.POST.items():
        # тк order_by всегда выставляеться в сессию в независимости от значения то мы его не добавляем
        if key != 'order_by' or key != 'csrfmiddlewaretoken':
            filter_dict.update({f'{key}': value})

    for key, value in filter_dict.items():
        if value:
            request.session[f'{key}'] = value
        elif (value == 0 or not value) and key in request.session:
            del request.session[f'{key}']
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

