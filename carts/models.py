from django.db import models
from uuid import uuid4

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    total_price = models.FloatField()
    user_id = models.ForeignKey()


class Cart_products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    quantity = models.IntegerField()
    cart_id = models.ForeignKey(Cart)
    product_id = models.ForeignKey()
