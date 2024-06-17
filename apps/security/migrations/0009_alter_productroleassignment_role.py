# Generated by Django 4.2.2 on 2024-06-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("security", "0008_delete_ideavote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productroleassignment",
            name="role",
            field=models.CharField(
                choices=[("Contributor", "Contributor"), ("Manager", "Product Manager"), ("Admin", "Product Admin")],
                default="Contributor",
                max_length=255,
            ),
        ),
    ]