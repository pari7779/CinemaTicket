from collections import UserList
from pyclbr import Class
from django.shortcuts import render
from user.models import User
import json
from rest_framework.generics import ListAPIView
from django.http.response import JsonResponse
from rest_framework.serializers import Serializer

# Create your views here.
Class UserList(ListAPIView):

queryset=User.objects.all()
Serializer_class= UserSerializer
 
 
