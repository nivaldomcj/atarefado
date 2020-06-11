from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from tasklist.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
