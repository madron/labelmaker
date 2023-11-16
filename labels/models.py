from copy import copy
from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
from . import utils


TEMPLATE_LAYOUT_DEFAULT = dict(
    sheet=dict(x=2, y=4, x_space=10, y_space=10),
    size=dict(x=85.60, y=53.98),
    text=dict(x1=0, x2=55, y1=0, y2=80),
    image=dict(x1=55, x2=100, y1=0, y2=80),
    style=dict(
        background=dict(x1=0, x2=100, y1=80, y2=100),
        image=dict(x1=55, x2=100, y1=80, y2=100),
    ),
)


def get_template_layout_default():
    return copy(TEMPLATE_LAYOUT_DEFAULT)


class Style(models.Model):
    name = models.CharField(_('name'), max_length=200)
    background = ColorField(blank=True)
    image = models.FileField(blank=True, upload_to=utils.get_style_image_path)

    class Meta:
        verbose_name = _('style')
        verbose_name_plural = _('styles')
        ordering = ['name']

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(_('name'), max_length=200)
    style = models.ForeignKey(
        Style, verbose_name=_('style'), on_delete=models.PROTECT, related_name='labels', db_index=True, null=True, blank=True,
    )
    text = models.TextField(blank=True)
    image = models.FileField(blank=True, upload_to=utils.get_label_image_path)

    class Meta:
        verbose_name = _('label')
        verbose_name_plural = _('labels')
        ordering = ['name']

    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(_('name'), max_length=50, primary_key=True)
    layout = models.JSONField(verbose_name=_('parameters'), default=get_template_layout_default)

    class Meta:
        verbose_name = _('template')
        verbose_name_plural = _('templates')
        ordering = ['name']

    def __str__(self):
        return self.name
