# Generated by Django 4.1.7 on 2023-03-14 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart_products",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="products.product"
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="products",
            field=models.ManyToManyField(
                related_name="cart",
                through="carts.Cart_products",
                to="products.product",
            ),
        ),
    ]