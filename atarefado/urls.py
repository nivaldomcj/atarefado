from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasklist import views

# Register routes for API
router = DefaultRouter()
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
    # Administrator Panel
    path('', admin.site.urls),

    # API Routes
    path('api/', include(router.urls)),

    # API Authentication
    path('api-auth/',  include('rest_framework.urls')),
]
