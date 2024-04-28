from rest_framework import serializers

from product_reviews.models import Product, Review


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('id', 'prodict_aisin')


class ProductModelSerializer(serializers.ModelSerializer):
    reviews = ReviewModelSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = "__all__"