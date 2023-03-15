from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False)
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    complement = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="address"
    )
