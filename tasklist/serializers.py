from django.contrib.auth.models import User
from rest_framework import serializers
from tasklist.models import NotificationModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser', 'is_staff',
                  'date_joined', 'last_login']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = ['id', 'user', 'text', 'sent_date', 'was_sent']
