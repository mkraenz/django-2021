from datetime import date, timedelta

from hypothesis import given, strategies
from hypothesis.extra.django import TestCase

from books.models import Book

tomorrow = date.today() + timedelta(days=1)
yesterday = date.today() - timedelta(days=1)
a_year_later = date.today() + timedelta(days=367)
a_year_ago = date.today() - timedelta(days=367)


class BookModelTests(TestCase):

    def test_was_published_today_for_today_is_true(self):
        today = date.today()
        book = Book(pub_date=today)
        self.assertTrue(book.was_published_today())

    @given(strategies.dates(tomorrow, a_year_later))
    def test_was_published_today_for_future_dates_is_false(self, future: date):
        book = Book(pub_date=future)
        self.assertFalse(book.was_published_today())

    @given(strategies.dates(a_year_ago, yesterday))
    def test_was_published_today_for_past_dates_is_false(self, past: date):
        book = Book(pub_date=past)
        self.assertFalse(book.was_published_today())
