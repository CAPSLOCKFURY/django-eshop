"""
 Author : Vadim Dembitskii (CAPSLOCKFURY)
 License : The MIT License
"""

from django.urls import path
from .views import CategorySpecificationsViewSet

urlpatterns = [
    path('category-specs/<int:pk>', CategorySpecificationsViewSet.as_view({'get': 'list'}))
]