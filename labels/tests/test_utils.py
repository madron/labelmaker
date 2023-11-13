from django.test import TestCase
from . import factories
from .. import utils


class GetStyleImagePathTest(TestCase):
    def test_svg(self):
        obj = factories.StyleFactory(id=1)
        self.assertEqual(utils.get_style_image_path(obj, 'nike.svg'), 'labels/style/1.svg')

    def test_jpg(self):
        obj = factories.StyleFactory(id=9)
        self.assertEqual(utils.get_style_image_path(obj, 'nike.jpg'), 'labels/style/9.jpg')
