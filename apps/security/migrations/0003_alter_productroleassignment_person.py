# Generated by Django 4.2.2 on 2023-09-26 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("talent", "0001_initial"),
        ("security", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productroleassignment",
            name="person",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="talent.person"),
        ),
    ]
