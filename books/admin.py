from django.contrib import admin

from .models import Book, Chapter


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 3


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ["title", "pub_date"]

    fieldsets = [
        (None, {"fields": ["title", "author"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChapterInline]
    list_display = ["title", "author", "pub_date", "was_published_today"]
    list_filter = ["pub_date"]
    search_fields = ["title", "author"]
