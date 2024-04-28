from django.db import models

from django.db import models


class Product(models.Model):
    aisin = models.CharField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(
        verbose_name="Created at", auto_now_add=True, editable=False, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated at", auto_now=True, editable=False, null=True
    )

    def __str__(self):
        return f"{self.aisin} - {self.title}"


class Review(models.Model):
    prodict_aisin = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        verbose_name='product',
        related_name='reviews',
        null=True,
    )
    title = models.CharField(max_length=255)
    review = models.TextField()
    created_at = models.DateTimeField(
        verbose_name="Created at", auto_now_add=True, editable=False, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated at", auto_now=True, editable=False, null=True
    )

    def __str__(self):
        return f"{self.id} - {self.title}"
