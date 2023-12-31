from copy import copy
from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
from . import constants
from . import utils


def get_template_layout_default():
    return copy(constants.TEMPLATE_LAYOUT_DEFAULT)


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
