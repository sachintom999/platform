# Generated by Django 4.2.2 on 2023-08-14 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("commerce", "0002_initial"),
        ("product_management", "0003_remove_product_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.organisation",
            ),
        ),
    ]