from django.test import TestCase
from . import factories


class StyleTest(TestCase):
    def test_str(self):
        style = factories.StyleFactory(name='nike')
        self.assertEqual(str(style), 'nike')


class LabelTest(TestCase):
    def test_str(self):
        label = factories.LabelFactory(name='air')
        self.assertEqual(str(label), 'air')
