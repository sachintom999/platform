# Generated by Django 4.2.2 on 2024-05-25 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product_management", "0039_challenge_attachments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="challenge",
            name="attachment",
        ),
    ]