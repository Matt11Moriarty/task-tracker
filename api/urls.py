from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet, SharedTrackerViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'shared-trackers', SharedTrackerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
