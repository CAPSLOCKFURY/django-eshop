"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from rest_framework.viewsets import ViewSet
from eshop.funcs import cart_id_get_or_create
from ..models import Product
from filters.models import Filter
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie


class ProductViewSet(ViewSet):

    def list(self, request, pk: int):
        products = Filter().get_filtered_products(request, pk)
        q = request.GET.get("q", "")
        products = products.filter(title__icontains=q)
        q_filter = Filter().get_specs_filters(request)
        for filter in q_filter:
            products = products.filter(**filter)
            if products:
                continue
            else:
                break
        res = ProductSerializer(products, many=True)
        return Response(res.data)


@api_view(['GET', 'POST'])
@ensure_csrf_cookie
def product_detail(request, pk: int):
    product = Product.objects.get(pk=pk)
    if request.method == "GET":
        res = ProductSerializer(product)
        return Response(res.data)

    if request.method == "POST":
        cart_id = cart_id_get_or_create(request)
        product.add_to_cart(cart_id)
        return Response({'id': cart_id})
