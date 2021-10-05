from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.book_details, name='book_details'),
    path('<int:book_id>/chapters/', views.chapters, name='chapters'),
    path('<int:book_id>/chapters/<int:chapter_numeral>',
         views.chapter_details, name='chapter_details'),
    path('add', views.add_book, name='add'),
]
