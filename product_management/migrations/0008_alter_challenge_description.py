# Generated by Django 4.2.2 on 2023-11-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0007_create_bug_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="description",
            field=models.TextField(),
        ),
    ]