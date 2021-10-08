from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.BookDetailsView.as_view(), name="book_details"),
    path("<int:pk>/chapters/", views.BookChaptersView.as_view(), name="chapters"),
    path(
        "<int:book_id>/chapters/<int:chapter_id>",
        views.chapter_details,
        name="chapter_details",
    ),
    path("add/", views.add_book, name="add"),
]
