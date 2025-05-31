from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Check if users already exist before creating
        if not User.objects.filter(email="john.doe@example.com").exists():
            user1 = User.objects.create(email="john.doe@example.com", name="John Doe", password="password123")
        else:
            user1 = User.objects.get(email="john.doe@example.com")

        if not User.objects.filter(email="jane.smith@example.com").exists():
            user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", password="password123")
        else:
            user2 = User.objects.get(email="jane.smith@example.com")

        # Create test teams
        Team.objects.create(name="Team Alpha", members=["John Doe", "Jane Smith"])
        Team.objects.create(name="Team Beta", members=["Alice", "Bob"])

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
