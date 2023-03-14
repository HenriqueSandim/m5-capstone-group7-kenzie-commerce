from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


# Create your models here.
class UserTypeChoice(models.TextChoices):
    CLIENTE = "Cliente"
    VENDEDOR = "Vendedor"
    ADMINISTRADOR = "Administrador"


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(max_length=127, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    cpf = models.CharField(max_length=11)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_type = models.CharField(
        choices=UserTypeChoice.choices,
        default=UserTypeChoice.CLIENTE,
        max_length=30
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    address = models.OneToOneField(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="address"
    )
