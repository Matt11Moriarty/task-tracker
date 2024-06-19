from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path("add/", UserViewSet.add_user, name="add_user"),
]