from rest_framework import serializers
from users.models import CustomUser
from tasks.models import Task
from sharing.models import SharedTracker

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SharedTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedTracker
        fields = '__all__'
