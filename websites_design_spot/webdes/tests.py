from django.test import TestCase
from .models import Webdes

# Create your tests here.

class WebdesTests(TestCase):
    """
    Here is defined an initial test that will run against the Webdes model
    """

    def test_str(self):
        test_name = Webdes(name='A web design')
        self.assertEqual(str(test_name), 'A web design')
