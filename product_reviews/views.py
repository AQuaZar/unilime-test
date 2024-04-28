from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
)

from product_reviews.models import Review, Product
from product_reviews.serializers import ProductModelSerializer


class ProductViewSet(
    RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
