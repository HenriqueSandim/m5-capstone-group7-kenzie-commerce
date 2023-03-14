from django.db import models
from uuid import uuid4

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    total_price = models.FloatField()
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cart"
    )

    products = models.ManyToManyField(
        "products.Product",
        through="Cart_products",
        related_name="cart"
    )


class Cart_products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
