from rest_framework import serializers, viewsets

from .models import Book, Chapter


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  # type: ignore
        model = Book
        fields = ["title", "author", "pub_date", "was_published_today", "chapter_set"]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  # type: ignore
        model = Chapter
        fields = ["title", "numeral", "book"]


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
