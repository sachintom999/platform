# Generated by Django 4.2.2 on 2024-05-28 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
        ("product_management", "0046_alter_productarea_attachments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="attachments",
            field=models.ManyToManyField(blank=True, to="common.fileattachment"),
        ),
    ]