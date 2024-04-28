from django.contrib import admin

from product_reviews.models import Product, Review


admin.site.register(Product)
admin.site.register(Review)
