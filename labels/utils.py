import io
import pathlib
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


def get_style_image_path(instance, filename):
    return 'labels/style/{}{}'.format(instance.pk, pathlib.Path(filename).suffix)


def get_label_image_path(instance, filename):
    return 'labels/label/{}{}'.format(instance.pk, pathlib.Path(filename).suffix)


def get_label_pdf(label, layout):
    file = io.BytesIO()
    c = canvas.Canvas(file, bottomup=False)
    # Canvas
    dx = 10
    dy = 10
    c.translate(dx * mm, dy * mm)
    c = draw_label(c, label, layout)
    c.translate(-dx * mm, -dy * mm)
    # # Canvas
    # dx = 10
    # dy = 70
    # c.translate(dx * mm, dy * mm)
    # c = draw_label(c, label, layout)
    # c.translate(-dx * mm, -dy * mm)
    # File
    c.showPage()
    c.save()
    file.seek(0)
    return file


def get_sheet_pdf(label, layout):
    file = io.BytesIO()
    c = canvas.Canvas(file, bottomup=False)
    # Canvas
    c = draw_label(c, 0, 0, label, layout)
    # File
    c.showPage()
    c.save()
    file.seek(0)
    return file


def draw_label(c, label, layout):
    print(layout)
    size_x = layout['size']['x']
    size_y = layout['size']['y']
    # removeme
    c.rect(0, 0, size_x * mm, size_y * mm)
    # Image
    x1 = layout['image']['x1'] * size_x / 100
    x2 = layout['image']['x2'] * size_x / 100
    y1 = layout['image']['y1'] * size_y / 100
    y2 = layout['image']['y2'] * size_y / 100
    # removeme
    c.rect(x1 * mm, y1 * mm, (x2 - x1) * mm, (y2 - y1) * mm, stroke=1, fill=0)
    c.saveState()
    c.scale(1,-1)
    c.drawImage(label.image.path, x1 * mm, -y2 * mm, width=(x2 - x1) * mm, height=(y2 - y1) * mm, preserveAspectRatio=True, mask='auto')
    c.restoreState()
    # Style
    style = label.style
    # Style background
    x1 = layout['style']['background']['x1'] * size_x / 100
    x2 = layout['style']['background']['x2'] * size_x / 100
    y1 = layout['style']['background']['y1'] * size_y / 100
    y2 = layout['style']['background']['y2'] * size_y / 100
    c.saveState()
    c.setFillColor(colors.HexColor(style.background))
    c.rect(x1 * mm, y1 * mm, (x2 - x1) * mm, (y2 - y1) * mm, stroke=0, fill=1)
    c.restoreState()
    # Style image
    x1 = layout['style']['image']['x1'] * size_x / 100
    x2 = layout['style']['image']['x2'] * size_x / 100
    y1 = layout['style']['image']['y1'] * size_y / 100
    y2 = layout['style']['image']['y2'] * size_y / 100
    # removeme
    c.rect(x1 * mm, y1 * mm, (x2 - x1) * mm, (y2 - y1) * mm, stroke=0, fill=1)
    # https://www.blog.pythonlibrary.org/2018/04/12/adding-svg-files-in-reportlab/
    # c.saveState()
    # c.scale(1,-1)
    # c.drawImage(style.image.path, x1 * mm, -y2 * mm, width=(x2 - x1) * mm, height=(y2 - y1) * mm, preserveAspectRatio=True, mask='auto')
    # c.restoreState()
    return c
