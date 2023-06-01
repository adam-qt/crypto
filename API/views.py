from django.shortcuts import render
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from data.models import Crypto
from articles.models import Article


class UserList(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class CryptoList(generics.ListCreateAPIView):
    queryset = Crypto.objects.all()
    serializer_class = serializers.CryptoSerializer


class CryptoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crypto.objects.all()
    serializer_class = serializers.CryptoSerializer
    lookup_field = 'slug'


def api_manual(request):

    return render(request, 'API/api_manual.html')
