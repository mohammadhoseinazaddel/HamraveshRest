from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Author(models.Model):
    author_name = models.CharField(max_length=20, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.author_name


class Book(models.Model):
    STORY = 'st'
    LESSON = 'ls'
    LANGUAGE = 'ln'
    categorie_choices = [
        (STORY, 'story'),
        (LESSON, 'Lesson'),
        (LANGUAGE, 'Language'),
    ]
    book_name = models.CharField(max_length=50, blank=False)
    author = models.ManyToManyField(Author)
    year_of_stablishing = models.DateField()
    category = models.CharField(max_length=2, choices=categorie_choices, default=STORY)

    def __unicode__(self):
        return self.book_name
