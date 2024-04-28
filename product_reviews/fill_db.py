import csv
import os

from product_reviews.models import Product, Review


def main():
    with open(os.path.join('product_reviews/Products.csv'), 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        products = dict()
        for row in reader:
            products[row[1]] = Product(aisin=row[1], title=row[0])

        Product.objects.bulk_create(products.values())

    with open(os.path.join('product_reviews/Reviews.csv'), 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        reviews = list()
        for row in reader:
            aisin = row[0]
            if aisin in products:
                reviews.append(
                    Review(
                        prodict_aisin_id=aisin,
                        title=row[1],
                        review=row[2],
                    )
                )

        Review.objects.bulk_create(reviews)


main()