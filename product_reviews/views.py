from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
)

from product_reviews.models import Review, Product
from product_reviews.serializers import ProductModelSerializer, ReviewModelSerializer, CreateReviewModelSerializer


class ProductViewSet(
    RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class ReviewViewSet(
    CreateModelMixin,
    GenericViewSet,
):
    queryset = Review.objects.all()
    serializer_class = CreateReviewModelSerializer
