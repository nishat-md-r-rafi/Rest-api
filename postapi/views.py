import pprint
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Post
from .serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth import authenticate
# Create your views here.


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)  # data is a dictionary
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error': 'username taken. choose another username'},
                status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password'])
        if user is None:
            return JsonResponse(
                {'error': 'unable to login. check username and password'},
                status=400)
        else:  # return user token
            try:
                token = Token.objects.get(user=user)
            except:  # if token not in db, create a new one
                ken = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
