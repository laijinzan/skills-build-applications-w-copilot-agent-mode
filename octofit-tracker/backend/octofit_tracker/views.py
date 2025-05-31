from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

# Update the queryset to use the codespace URL
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(email__icontains="@vigilant-cod-5gwrxpqwggqf7q9j-8000.app.github.dev")

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# Allow HTTPS certificate issues to be bypassed
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
