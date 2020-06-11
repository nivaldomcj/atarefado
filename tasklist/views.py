from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from tasklist.serializers import (UserSerializer,
                                  NotificationSerializer,
                                  TaskAdminSerializer,
                                  TaskUserSerializer)
from tasklist.models import NotificationModel, TaskModel


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Only notifications for current user will be displayed
        return NotificationModel.objects.filter(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        # Only tasks for current user will be displayed
        return TaskModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # When a task is created, should be assigned to the logged user
        # Except when is a administrator creating it, he can do for everyone
        if not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return TaskAdminSerializer

        return TaskUserSerializer
