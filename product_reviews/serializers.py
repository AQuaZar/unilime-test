from rest_framework import serializers

from product_reviews.models import Product, Review


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('id', 'prodict_aisin')


def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')


class CreateReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('prodict_aisin', 'title', 'review',)
        extra_kwargs = {'prodict_aisin': {'required': True}}


class ProductModelSerializer(serializers.ModelSerializer):
    reviews = ReviewModelSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = "__all__"