
import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateField("date published")

    def __str__(self):
        return f'{self.title} --- {self.author}'

    def was_published_today(self) -> bool:
        return self.pub_date == datetime.date.today()


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    numeral = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.book.title} --- {self.numeral} - {self.title}'
