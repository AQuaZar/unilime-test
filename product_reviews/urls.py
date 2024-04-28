from django.urls import path, include
from rest_framework import routers

from product_reviews.views import ProductViewSet, ReviewViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register("product", ProductViewSet, basename="product-api")
router.register("review", ReviewViewSet, basename="review-api")

urlpatterns = [
    path("", include(router.urls), name="product-api"),
]
