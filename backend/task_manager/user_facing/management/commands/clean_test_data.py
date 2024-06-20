from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from user_facing.models import UserProfile, Task
from admin_facing.models import App

class Command(BaseCommand):

    help = "Delete all test data"

    def handle(self, *args, **kwargs):
        User.objects.exclude(is_staff=False, is_superuser=False).delete()
        Task.objects.all().delete()
        UserProfile.objects.all().delete()
        App.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all test data.'))
