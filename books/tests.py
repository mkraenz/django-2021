from datetime import date, timedelta

from hypothesis import given, strategies
from hypothesis.extra.django import TestCase

from books.models import Book


class BookModelTests(TestCase):

    def test_was_published_today_for_today_is_true(self):
        today = date.today()
        book = Book(pub_date=today)
        self.assertTrue(book.was_published_today())

    @given(strategies.integers(1, 1000))
    def test_was_published_today_for_future_dates_is_false(self, days: int):
        future = date.today() + timedelta(days=days)
        book = Book(pub_date=future)
        self.assertFalse(book.was_published_today())

    @given(strategies.integers(-1000, -1))
    def test_was_published_today_for_past_dates_is_false(self, days: int):
        past = date.today() - timedelta(days=days)
        book = Book(pub_date=past)
        self.assertFalse(book.was_published_today())
