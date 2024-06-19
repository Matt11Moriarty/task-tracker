from django.shortcuts import render
from .services import UserService
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions



class UserViewSet(viewsets.ModelViewSet):


    def add_user(request):
        data = request
        UserService.add_user(data)