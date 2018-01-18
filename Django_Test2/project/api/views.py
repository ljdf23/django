from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from project.api.serializers import UserSerializer
# Create your views here.

class UserViewSet (viewsets.ModelViewSet):
    """
    Api Endpoint that allows users to be viewed or edited
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer