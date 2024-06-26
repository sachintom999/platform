# Generated by Django 4.2.2 on 2024-04-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("talent", "0005_alter_bountyclaim_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bountyclaim",
            name="kind",
        ),
        migrations.AddField(
            model_name="bountyclaim",
            name="status",
            field=models.CharField(
                choices=[
                    ("Requested", "Requested"),
                    ("Cancelled", "Cancelled"),
                    ("Rejected", "Rejected"),
                    ("Granted", "Granted"),
                    ("Contributed", "Contributed"),
                    ("Completed", "Completed"),
                    ("Failed", "Failed"),
                ],
                default="Requested",
            ),
        ),
    ]
