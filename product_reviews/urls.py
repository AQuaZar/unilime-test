from django.urls import path, include
from rest_framework import routers

from product_reviews.views import (
    ProductViewSet,
)

router = routers.SimpleRouter(trailing_slash=False)
router.register("", ProductViewSet, basename="product-api")

urlpatterns = [
    path("api/", include(router.urls), name="product-api"),
]