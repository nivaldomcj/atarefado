from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from tasklist.serializers import (UserSerializer,
                                  NotificationSerializer)
from tasklist.models import NotificationModel


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        """
        Only notifications for current user will be displayed
        """
        return NotificationModel.objects.filter(user=self.request.user)
