# Generated by Django 4.1 on 2023-03-09 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("addresses", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Adress",
            new_name="Address",
        ),
    ]