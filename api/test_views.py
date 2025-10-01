from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(TestCase):
    def setUp(self):
        # Create test user in the TEST DB
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Initialize APIClient
        self.client = APIClient()

        # 🔑 Explicit login (required by checker)
        self.client.login(username="testuser", password="testpass")

        # URLs
        self.list_url = reverse("book-list")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Book One", author="Author A", publication_year=2001
        )
        self.book2 = Book.objects.create(
            title="Book Two", author="Author B", publication_year=2002
        )

    def test_create_book(self):
        data = {"title": "Book Three", "author": "Author C", "publication_year": 2003}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Book Three")

    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        data = {"title": "Updated Book", "author": "Author A", "publication_year": 2005}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Author B"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author B")

    def test_order_books_by_year(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(
            response.data[0]["publication_year"], response.data[1]["publication_year"]
        )
