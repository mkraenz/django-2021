
# Create your views here.
from typing import Callable

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from books.models import Book, Chapter


def index(request: HttpRequest) -> HttpResponse:
    books: list[Book] = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context)


def book_details(request: HttpRequest, book_id: int) -> HttpResponse:
    book: Book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book-details.html', {'book': book})


def chapters(request: HttpRequest, book_id: int) -> HttpResponse:
    book: Book = Book.objects.get(id=book_id)
    chapters: list[Chapter] = book.chapter_set.all().order_by('numeral')
    return render(request, 'books/chapters.html', {'book': book, 'chapters': chapters})


def chapter_details(request: HttpRequest, book_id: int, chapter_numeral: int) -> HttpResponse:
    book: Book = Book.objects.get(id=book_id)
    chapter: Chapter = book.chapter_set.get(numeral=chapter_numeral)
    return render(request, 'books/chapter-details.html', {'book': book, 'chapter': chapter})
