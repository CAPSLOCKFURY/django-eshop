"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from rest_framework.viewsets import ViewSet
from ..models import Cart
from .serializers import CartSerializer
from rest_framework.response import Response


class CartViewSet(ViewSet):

    def list(self, request):
        if 'cart_id' in request.session:
            user_cart = Cart.objects.filter(cart_id=request.session['cart_id'], order_id__isnull=True)
            res = CartSerializer(user_cart, many=True)
            return Response(res.data)
        return Response({})
