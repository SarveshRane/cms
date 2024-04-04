from rest_framework import serializers
from .models import User, ContentItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'country', 'pincode']
        extra_kwargs = {'password': {'write_only': True}}


class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = ['id', 'title', 'body', 'summary', 'categories', 'author']
