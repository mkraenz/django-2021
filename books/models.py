import datetime

from django.contrib import admin
from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateField("date published")

    objects: "models.Manager[Book]"
    chapter_set: "models.Manager[Chapter]"

    def __str__(self):
        return f"{self.title} --- {self.author}"

    @admin.display(boolean=True, ordering="pub_date", description="Published today")
    def was_published_today(self) -> bool:
        return self.pub_date == datetime.date.today()


class Chapter(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    numeral = models.IntegerField(default=1)

    objects: "models.Manager[Chapter]"

    def __str__(self):
        return f"{self.book.title} --- {self.numeral} - {self.title}"
