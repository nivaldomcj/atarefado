from django.contrib.auth.models import User
from rest_framework import serializers
from tasklist.models import NotificationModel, TaskModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser', 'is_staff',
                  'date_joined', 'last_login']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = ['id', 'user', 'text', 'sent_date', 'was_sent']


class TaskUserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TaskModel
        fields = ['id', 'user', 'title', 'description', 'due_date', 'is_done']


class TaskAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'user',
                  'title', 'description', 'due_date', 'is_done']
