from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


class Style(models.Model):
    name = models.CharField(_('name'), max_length=200)
    background = ColorField(blank=True)

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

    class Meta:
        verbose_name = _('label')
        verbose_name_plural = _('labels')
        ordering = ['name']

    def __str__(self):
        return self.name
