
# Create your views here.
from typing import Callable

from django.http import HttpRequest, HttpResponse

from books.models import Book, Chapter


def index(request: HttpRequest) -> HttpResponse:
    books: list[Book] = Book.objects.all()
    withLink: Callable[[Book],
                       str] = lambda x: f'<li><a href="/books/{x.id}">{x}</a></li>'
    book_list = ''.join([withLink(book) for book in books])
    return HttpResponse(f"<ul>{book_list}</ul>")


def book_details(request: HttpRequest, book_id: int) -> HttpResponse:
    book: Book = Book.objects.get(id=book_id)
    return HttpResponse(book)


def chapters(request: HttpRequest, book_id: int) -> HttpResponse:
    book: Book = Book.objects.get(id=book_id)
    chapters: list[Chapter] = book.chapter_set.all()
    chapter_list = ', '.join([str(chapter) for chapter in chapters])
    return HttpResponse(f"<p>{book}</p><p>{chapter_list}</p>")


def chapter_details(request: HttpRequest, book_id: int, chapter_numeral: int) -> HttpResponse:
    book: Book = Book.objects.get(id=book_id)
    chapter: Chapter = book.chapter_set.get(numeral=chapter_numeral)
    return HttpResponse(f"Chapter {str(chapter)}")
