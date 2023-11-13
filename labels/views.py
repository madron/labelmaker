from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.http import Http404
# from django.http import HttpResponse
# from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from . import models


class LabelTemplateView(PermissionRequiredMixin, DetailView):
    model = models.Label
    pk_url_kwarg = 'object_id'
    permission_required = 'labels.change_label'
    template_name = 'labels/label_template.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['template'] = self.template
        return data

    def get_object(self, queryset=None):
        self.template = get_object_or_404(models.Template, pk=self.kwargs['template'])
        return super().get_object(queryset=queryset)
