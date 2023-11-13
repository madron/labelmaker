import pathlib


def get_style_image_path(instance, filename):
    return 'labels/style/{}{}'.format(instance.pk, pathlib.Path(filename).suffix)
