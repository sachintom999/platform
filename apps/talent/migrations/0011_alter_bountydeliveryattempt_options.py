# Generated by Django 4.2.2 on 2024-05-28 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("talent", "0010_remove_bountydeliveryattempt_attachment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bountydeliveryattempt",
            options={"ordering": ("-created_at",)},
        ),
    ]
