from django.shortcuts import render
from .services import UserService
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
import json
from django.http import HttpResponse, JsonResponse



class UserViewSet(viewsets.ModelViewSet):


    def add_user(request):
        data = json.loads(request.body)
        response_data = UserService.add_user(data)
        response = {}
        response['status'], response['insertedId'] = 200, str(response_data.inserted_id)

        return JsonResponse(response)