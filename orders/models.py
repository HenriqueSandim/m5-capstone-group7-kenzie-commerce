from django.db import models
import uuid


class StatusOptions(models.TextChoices):
    DEFAULT = "Pedido realizado"
    EM_ANDAMENTO = "Em andamento"
    ENTREGUE = "Entregue"


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False) 
    order_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(
        max_length=30,
        default=StatusOptions.DEFAULT,
        choices=StatusOptions.choices
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders"
    )

    products = models.ManyToManyField(
        "products.Product",
        through="orders.OrderProducts",
        related_name="product_orders"
    )


class OrderProducts(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False)
    quantity = models.IntegerField()

    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="order_products"
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="user_order_products",
    )

    def __str__(self) -> str:
        return f"<ProductOrder [{self.id}] - {self.quantity}>"
