from datetime import date

from django.test import TestCase

from books.models import Book


class BookModelTests(TestCase):

    def test_was_published_today_for_today_is_true(self):
        time = date.today()
        book = Book(pub_date=time)
        self.assertTrue(book.was_published_today())
