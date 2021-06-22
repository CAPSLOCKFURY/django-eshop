"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import CategoryRelatedSpecificationsSerializer
from main.models import Category


class CategorySpecificationsViewSet(ViewSet):

    def list(self, request, pk: int):
        category = Category.objects.get(pk=pk)
        res = CategoryRelatedSpecificationsSerializer(category)
        return Response(res.data)
