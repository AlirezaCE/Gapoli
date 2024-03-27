# Create a new management command file, e.g., reset_user_attribute.py
# Inside the file, define your management command

from django.core.management.base import BaseCommand
from account.models import User
from post.models import Post

class Command(BaseCommand):
    help = 'Reset a specific attribute to zero for all users'

    def handle(self, *args, **kwargs):
        # Fetch all users
        users = User.objects.all()

        # Iterate over each user and update the attribute
        for user in users:
            user.post_count = Post.objects.filter(created_by = user).count()  # Replace attribute_to_reset with the name of your attribute
            user.save()

        self.stdout.write(self.style.SUCCESS('Attribute reset successfully for all users'))
