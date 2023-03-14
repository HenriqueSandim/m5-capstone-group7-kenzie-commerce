# Generated by Django 4.1.7 on 2023-03-14 12:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0002_product_is_avaliable"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("order_at", models.DateTimeField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pedido realizado", "Default"),
                            ("Em andamento", "Em Andamento"),
                            ("Entregue", "Entregue"),
                        ],
                        default="Pedido realizado",
                        max_length=30,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderProducts",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_products",
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_order_products",
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                related_name="product_orders",
                through="orders.OrderProducts",
                to="products.product",
            ),
        ),
    ]
