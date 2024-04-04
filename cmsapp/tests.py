from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, ContentItem
from .serializers import UserSerializer, ContentItemSerializer


class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'Test1234', 'first_name': 'Test', 'last_name': 'User', 'phone': '1234567890', 'pincode': '123456'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    # Write more test cases for user operations


class ContentItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='Test1234', first_name='Test', last_name='User', phone='1234567890', pincode='123456')
        self.client.force_authenticate(user=self.user)

    def test_create_content_item(self):
        url = reverse('contentitem-list')
        data = {'title': 'Test Title', 'body': 'Test Body', 'summary': 'Test Summary', 'categories': 'Test Category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContentItem.objects.count(), 1)
        self.assertEqual(ContentItem.objects.get().title, 'Test Title')

    # Write more test cases for content item operations
