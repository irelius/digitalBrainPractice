from django.core.management.base import BaseCommand
from app.models import Task, User

class Command(BaseCommand):
    help = 'Seed data for the app'

    def handle(self, *args, **options):
        demo_user = User.objects.create(username="demo-user", password="demo-password")

        Task.objects.create(task="Create a new task", user=demo_user)
        Task.objects.create(task="Complete a task", user=demo_user)
