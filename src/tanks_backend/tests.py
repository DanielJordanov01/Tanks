import django
from django.test import TestCase


class RequirementsTest(TestCase):

    def test_django_version(self):
        self.assertEqual('2.2.1', django.get_version())
