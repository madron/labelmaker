import io
import pathlib
from reportlab.pdfgen import canvas



def get_style_image_path(instance, filename):
    return 'labels/style/{}{}'.format(instance.pk, pathlib.Path(filename).suffix)


def get_label_image_path(instance, filename):
    return 'labels/label/{}{}'.format(instance.pk, pathlib.Path(filename).suffix)


def get_label_pdf(label, layout):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    # Canvas
    p.drawString(100, 500, "Hello world.")

    # Buffer
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
