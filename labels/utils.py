import io
from pathlib import Path
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.lib import pagesizes
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg


def get_style_image_path(instance, filename):
    return 'labels/style/{}{}'.format(instance.pk, Path(filename).suffix)


def get_label_image_path(instance, filename):
    return 'labels/label/{}{}'.format(instance.pk, Path(filename).suffix)


def get_label_pdf(label, layout):
    return get_sheet_pdf(labels=[label], layout=layout)


def get_sheet_pdf(labels, layout):
    pagesize = getattr(pagesizes, layout['sheet']['format'])
    file = io.BytesIO()
    c = canvas.Canvas(file, pagesize=pagesize, bottomup=False)
    # data
    sheet_labels_x = layout['sheet']['x']
    sheet_labels_y = layout['sheet']['y']
    sheet_space_x = layout['sheet']['space_x']
    sheet_space_y = layout['sheet']['space_y']
    start_x, start_y = get_start_label_x_y(layout)
    labels = list(labels)
    while labels:
        for y in range(sheet_labels_y):
            for x in range(sheet_labels_x):
                label = labels.pop(0)
                # generate label
                c.saveState()
                label_x, label_y = get_label_x_y(start_x, start_y, x, y, layout)
                c.translate(label_x * mm, label_y * mm)
                if sheet_space_x >= 5 and sheet_space_y >=5:
                    c = draw_reference(c, layout)
                c = draw_label(c, label, layout)
                c.restoreState()
                if not labels:
                    break
            if not labels:
                break
        c.showPage()
    c.save()
    file.seek(0)
    return file


def draw_reference(c, layout):
    size_x = layout['size']['x']
    size_y = layout['size']['y']
    # Horizontal
    c.rect(          -4 * mm,           0, 3 * mm, 0)
    c.rect((size_x + 1) * mm,           0, 3 * mm, 0)
    c.rect(          -4 * mm, size_y * mm, 3 * mm, 0)
    c.rect((size_x + 1) * mm, size_y * mm, 3 * mm, 0)
    # Vertical
    c.rect(          0,           -4 * mm, 0, 3 * mm)
    c.rect(          0, (size_y + 1) * mm, 0, 3 * mm)
    c.rect(size_x * mm,           -4 * mm, 0, 3 * mm)
    c.rect(size_x * mm, (size_y + 1) * mm, 0, 3 * mm)
    return c


def draw_label(c, label, layout):
    size_x = layout['size']['x']
    size_y = layout['size']['y']
    # Image
    x1 = layout['image']['x1'] * size_x / 100
    x2 = layout['image']['x2'] * size_x / 100
    y1 = layout['image']['y1'] * size_y / 100
    y2 = layout['image']['y2'] * size_y / 100
    if label.image:
        draw_image(c, label.image.path, x1, x2, y1, y2)
    # Style
    if label.style:
        style = label.style
        # background
        x1 = layout['style']['background']['x1'] * size_x / 100
        x2 = layout['style']['background']['x2'] * size_x / 100
        y1 = layout['style']['background']['y1'] * size_y / 100
        y2 = layout['style']['background']['y2'] * size_y / 100
        if style.background:
            c.saveState()
            c.setFillColor(colors.HexColor(style.background))
            c.rect(x1 * mm, y1 * mm, (x2 - x1) * mm, (y2 - y1) * mm, stroke=0, fill=1)
            c.restoreState()
        # image
        x1 = layout['style']['image']['x1'] * size_x / 100
        x2 = layout['style']['image']['x2'] * size_x / 100
        y1 = layout['style']['image']['y1'] * size_y / 100
        y2 = layout['style']['image']['y2'] * size_y / 100
        if style.image:
            draw_image(c, style.image.path, x1, x2, y1, y2)
    return c


def draw_image(c, image_path, x1, x2, y1, y2):
    c.saveState()
    c.scale(1,-1)
    if Path(image_path).suffix == '.svg':
        drawing = svg2rlg(image_path)
        box_x = (x2 -x1) * mm
        box_y = (y2 -y1) * mm
        scale_x = box_x / drawing.width
        scale_y = box_y / drawing.height
        scale = min(scale_x, scale_y)
        drawing.scale(scale, scale)
        scaled_x = drawing.width * scale
        scaled_y = drawing.height * scale
        x = x1 * mm + ((x2 - x1) * mm - scaled_x) / 2
        y = - y1 * mm - ((y2 - y1) * mm - scaled_y) / 2 - scaled_y
        renderPDF.draw(drawing, c, x, y)
    else:
        c.drawImage(image_path, x1 * mm, -y2 * mm, width=(x2 - x1) * mm, height=(y2 - y1) * mm, preserveAspectRatio=True, mask='auto')
    c.restoreState()


def get_start_label_x_y(layout):
    pagesize = getattr(pagesizes, layout['sheet']['format'])
    sheet_size_x = pagesize[0] / mm
    sheet_size_y = pagesize[1] / mm
    sheet_labels_x = layout['sheet']['x']
    sheet_labels_y = layout['sheet']['y']
    label_size_x = layout['size']['x']
    label_size_y = layout['size']['y']
    sheet_space_x = layout['sheet']['space_x']
    sheet_space_y = layout['sheet']['space_y']
    total_x = sheet_labels_x * label_size_x + (sheet_labels_x -1) * sheet_space_x
    total_y = sheet_labels_y * label_size_y + (sheet_labels_y -1) * sheet_space_y
    x = (sheet_size_x - total_x) / 2
    y = (sheet_size_y - total_y) / 2
    return round(x, 6), round(y, 6)


def get_label_x_y(start_x, start_y, x, y, layout):
    label_size_x = layout['size']['x']
    label_size_y = layout['size']['y']
    sheet_space_x = layout['sheet']['space_x']
    sheet_space_y = layout['sheet']['space_y']
    x = start_x + x * (label_size_x + sheet_space_x )
    y = start_y + y * (label_size_y + sheet_space_y )
    return round(x, 6), round(y, 6)
