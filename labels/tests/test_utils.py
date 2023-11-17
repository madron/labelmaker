from copy import copy
from django.test import TestCase
from . import factories
from .. import constants
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


class GetLabelImagePathTest(TestCase):
    def test_png(self):
        obj = factories.LabelFactory(id=1)
        self.assertEqual(utils.get_label_image_path(obj, 'air.png'), 'labels/label/1.png')

    def test_jpg(self):
        obj = factories.LabelFactory(id=9)
        self.assertEqual(utils.get_label_image_path(obj, 'air.jpg'), 'labels/label/9.jpg')


class GetLabelPdfTest(TestCase):
    def test_ok(self):
        label = factories.LabelFactory()
        layout = copy(constants.TEMPLATE_LAYOUT_DEFAULT)
        pdf = utils.get_label_pdf(label=label, layout=layout)


class GetStartLabelXYTest(TestCase):
    def test_2_4(self):
        layout = copy(constants.TEMPLATE_LAYOUT_DEFAULT)
        layout = dict(
            sheet=dict(format='A4', x=2, y=4, space_x=10, space_y=10),
            size=dict(x=85.60, y=53.98),
        )
        self.assertEqual(utils.get_start_label_x_y(layout), (14.4, 25.54))


class GetLabelXYTest(TestCase):
    def test_2_4(self):
        layout = dict(
            sheet=dict(space_x=20, space_y=20),
            size=dict(x=80, y=50),
        )
        self.assertEqual(utils.get_label_x_y(20, 20, 0, 0, layout), (20, 20))
        self.assertEqual(utils.get_label_x_y(20, 20, 1, 0, layout), (120, 20))
        self.assertEqual(utils.get_label_x_y(20, 20, 0, 1, layout), (20, 90))
        self.assertEqual(utils.get_label_x_y(20, 20, 1, 1, layout), (120, 90))
