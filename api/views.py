from rest_framework import viewsets
from users.models import CustomUser
from tasks.models import Task
from sharing.models import SharedTracker
from .serializers import UserSerializer, TaskSerializer, SharedTrackerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SharedTrackerViewSet(viewsets.ModelViewSet):
    queryset = SharedTracker.objects.all()
    serializer_class = SharedTrackerSerializer