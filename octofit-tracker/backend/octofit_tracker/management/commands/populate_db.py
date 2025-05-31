from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Ensure users are saved before creating related objects
        user1, created = User.objects.get_or_create(email="john.doe@example.com", defaults={"name": "John Doe", "password": "password123"})
        user2, created = User.objects.get_or_create(email="jane.smith@example.com", defaults={"name": "Jane Smith", "password": "password123"})

#Test
        # Create test activities
        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Create test workouts
        Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session to start the day.")
        Workout.objects.create(name="HIIT", description="High-intensity interval training for advanced users.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
