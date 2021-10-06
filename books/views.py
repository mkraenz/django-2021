# Create your views here.
from datetime import date

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from books.models import Book, Chapter


class IndexView(generic.ListView):
    template_name = "books/index.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter(pub_date__lte=date.today()).order_by("title")


class BookDetailsView(generic.DetailView):
    template_name = "books/book_details.html"
    model = Book

    def get_queryset(self) -> "QuerySet[Book]":
        return Book.objects.filter(pub_date__lte=date.today())


class BookChaptersView(generic.DetailView):
    template_name = "books/chapters.html"
    model = Book


def chapter_details(
    request: HttpRequest, book_id: int, chapter_numeral: int
) -> HttpResponse:
    book = Book.objects.get(id=book_id)
    chapter: Chapter = book.chapter_set.get(numeral=chapter_numeral)
    return render(
        request, "books/chapter_details.html", {"book": book, "chapter": chapter}
    )


def add_book(request: HttpRequest) -> HttpResponse:
    title: str = request.POST["title"]
    author: str = request.POST["author"]
    book = Book(title=title, author=author, pub_date=date.today())
    book.save()
    return HttpResponseRedirect(reverse("books:book_details", args=(book.id,)))
