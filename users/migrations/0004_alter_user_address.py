# Generated by Django 4.1 on 2023-03-12 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("addresses", "0002_rename_adress_address"),
        ("users", "0003_alter_user_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="address",
            field=models.OneToOneField(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="addresses.address",
            ),
        ),
    ]