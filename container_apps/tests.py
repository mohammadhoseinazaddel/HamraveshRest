from django.test import TestCase
from .models import *
import datetime

# modeltest
class ContainerTest(TestCase):
    def setUp(self):
        ContainerApps.objects.create(
            name='test',image='test',command='ls',envs='ss')

