# Generated by Django 5.0.3 on 2024-03-17 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0005_post_comment_count_comment_post_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("-created_at",)},
        ),
    ]