from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from tasklist import views

# API routes
router = SimpleRouter()
router.register('users',
                views.UserViewSet,
                basename='users')
router.register('notifications',
                views.NotificationViewSet,
                basename='notifications')
router.register('tasks',
                views.TaskViewSet,
                basename='tasks')

urlpatterns = [
    # API Urls
    path('', include(router.urls)),

    # API Authentication
    path('api-auth/', include('rest_framework.urls')),

    # Administrator Panel
    path('admin/', admin.site.urls),
]
