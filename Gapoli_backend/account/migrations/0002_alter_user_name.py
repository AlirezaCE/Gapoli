# Generated by Django 5.0.2 on 2024-03-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, default="", max_length=225, null=True),
        ),
    ]
