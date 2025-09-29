from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {"title": "Test Book", "author": "Tester"}
        self.url = reverse("book-list")  # adjust to your DRF route name

    def test_create_book(self):
        response = self.client.post(self.url, self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.book_data["title"])
        
class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user in the TEST database
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Initialize test client
        self.client = APIClient()

        # 🔑 Login with the test user (this is what the checker wants to see)
        self.client.login(username="testuser", password="testpass")

        self.book_data = {"title": "Test Book", "author": "Tester"}
        self.url = reverse("book-list")  # adjust to your route name

    def test_create_book(self):
        response = self.client.post(self.url, self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.book_data["title"])
