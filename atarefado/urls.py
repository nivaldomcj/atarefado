from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasklist import views

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    # API Urls
    path('', include(router.urls)),

    # API Authentication
    path('api-auth/', include('rest_framework.urls')),

    # Administrator Panel
    path('admin/', admin.site.urls),
]
