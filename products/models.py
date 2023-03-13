from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    inventory = models.IntegerField()
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
