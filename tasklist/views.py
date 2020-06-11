from django.contrib.auth.models import User
from rest_framework import (viewsets,
                            permissions)
from rest_framework.response import Response

from tasklist.serializers import (UserSerializer,
                                  NotificationSerializer,
                                  TaskSerializer,
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
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        # When listing, return tasks only that belongs to logged user
        queryset = TaskModel.objects.filter(user=request.user)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        # When querying, return tasks only that belongs to logged user
        # Except if is a administrator logged in
        if not self.request.user.is_superuser:
            return TaskModel.objects.filter(user=self.request.user)

        return TaskModel.objects.all()

    def perform_create(self, serializer):
        # When creating, assign it to logged user
        # Except when is a administrator creating it
        if not self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

    def get_serializer_class(self):
        # Administrators can see/edit all fields, but user not
        if self.request.user.is_superuser:
            return TaskSerializer
        return TaskUserSerializer
