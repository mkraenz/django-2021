from datetime import date, timedelta

from django.urls.base import reverse
from django.utils import formats
from django.utils.translation import activate
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


def create_book(title: str, age_in_days: int, author: str) -> Book:
    pub_date = date.today() + timedelta(days=-age_in_days)
    return Book.objects.create(title=title, author=author, pub_date=pub_date)


class BookIndexViewTests(TestCase):
    def test_no_books(self):
        activate("en-us")
        response = self.client.get(reverse("books:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No books found")
        self.assertQuerysetEqual(response.context["books"], [])

    def test_displays_books(self):
        yesterdays_book = create_book("yesterdays book", 1, "Fred Flintstone")
        todays_book = create_book("todays book", 0, "Boones")

        response = self.client.get(reverse("books:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, yesterdays_book.title)
        self.assertContains(response, yesterdays_book.author)
        self.assertContains(response, todays_book.title)
        self.assertContains(response, todays_book.author)
        self.assertQuerysetEqual(response.context["books"], [todays_book, yesterdays_book])  # type: ignore

    def test_ignores_books_published_in_the_future(self):
        future_book = create_book("future book", -1, "Doctor Zoidberg")
        future_book2 = create_book("future book 2", -300, "Bender")
        todays_book = create_book("todays Book", 0, "Boones")

        response = self.client.get(reverse("books:index"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, future_book.title)
        self.assertNotContains(response, future_book.author)
        self.assertNotContains(response, future_book2.title)
        self.assertNotContains(response, future_book2.author)
        self.assertContains(response, todays_book.title)
        self.assertQuerysetEqual(response.context["books"], [todays_book])  # type: ignore


class BookDetailsViewTests(TestCase):
    def test_displays_book_details_for_today(self):
        book = create_book("book title", 0, "book author")
        response = self.client.get(reverse("books:book_details", args=[book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, book.title)
        self.assertContains(response, book.author)
        # format reference: https://strftime.org/
        self.assertContains(response, book.pub_date.strftime("%b. %-d, %Y"))

    @given(strategies.integers(0, 10))
    def test_displays_details_for_past(self, days: int):
        book = create_book("book title", days, "book author")

        response = self.client.get(reverse("books:book_details", args=[book.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, book.title)
        self.assertContains(response, book.author)
        self.assertContains(response, formats.date_format(book.pub_date, "DATE_FORMAT"))

    @given(strategies.integers(1, 367))
    def test_404_Not_Found_for_future(self, days_in_the_future: int):
        book = create_book("book title", -days_in_the_future, "book author")
        response = self.client.get(reverse("books:book_details", args=[book.id]))
        self.assertEqual(response.status_code, 404)
