from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User, ContentItem
from .serializers import UserSerializer, ContentItemSerializer
from .permissions import IsOwnerOrAdmin


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContentItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ContentItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer
    permission_classes = [IsOwnerOrAdmin]
