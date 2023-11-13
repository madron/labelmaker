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


class GetLabelImagePathTest(TestCase):
    def test_png(self):
        obj = factories.LabelFactory(id=1)
        self.assertEqual(utils.get_label_image_path(obj, 'air.png'), 'labels/label/1.png')

    def test_jpg(self):
        obj = factories.LabelFactory(id=9)
        self.assertEqual(utils.get_label_image_path(obj, 'air.jpg'), 'labels/label/9.jpg')
