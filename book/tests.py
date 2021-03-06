from django.test import TestCase
from .models import *
import datetime

# modeltest
class booktest(TestCase):
    def setUp(self):
        Book.objects.create(
            book_name='test',year_of_stablishing=datetime.date(2010, 1, 2),category='ls')

class authortest(TestCase):
    def setUp(self):
        Book.objects.create(
            author_name='test',user='test')

