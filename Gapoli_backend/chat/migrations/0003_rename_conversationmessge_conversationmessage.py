# Generated by Django 5.0.3 on 2024-03-20 13:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_alter_conversation_id_alter_conversationmessge_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ConversationMessge",
            new_name="ConversationMessage",
        ),
    ]