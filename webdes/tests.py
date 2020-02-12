from django.test import TestCase
from .models import Webdes

class WebdesTests(TestCase):
    def setUp(self):
        Webdes.objects.create(name="Eco Mug Product Website", category="Event")
        Webdes.objects.create(name="Glasses Collection Website", category="Professional")

    def test_webdes_has_category(self):
        """Webdes that have category are correctly selected"""
        mugWeb = Webdes.objects.get(name="Eco Mug Product Website")
        glassesWeb = Webdes.objects.get(name="Glasses Collection Website")
        self.assertEqual(mugWeb.has(), 'This design has category "Event"')
        self.assertEqual(glassesWeb.has(), 'This design has category "Professional"')