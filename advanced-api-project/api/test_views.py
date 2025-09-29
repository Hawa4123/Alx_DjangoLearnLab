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
