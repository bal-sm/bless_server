from bismillah_on_py import bismillah
from django.test import TestCase

from .models import Ayat


class BasmallahTestCase(TestCase):
    def setUp(self):
        Ayat.objects.create(text=bismillah.the_sentence)

    def test_basmallah_exist(self):
        aya_teu = Ayat.objects.get(text=bismillah.the_sentence)
        self.assertEqual(aya_teu.text, bismillah.the_sentence)
