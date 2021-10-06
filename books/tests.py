from datetime import date, timedelta

from django.test import TestCase

from books.models import Book


class BookModelTests(TestCase):

    def test_was_published_today_for_today_is_true(self):
        today = date.today()
        book = Book(pub_date=today)
        self.assertTrue(book.was_published_today())

    def test_was_published_today_for_yesterday_is_false(self):
        yesterday = date.today() - timedelta(days=1)
        book = Book(pub_date=yesterday)
        self.assertFalse(book.was_published_today())

    def test_was_published_today_for_tomorrow_is_false(self):
        tomorrow = date.today() + timedelta(days=1)
        book = Book(pub_date=tomorrow)
        self.assertFalse(book.was_published_today())
