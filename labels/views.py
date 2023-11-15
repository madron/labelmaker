from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.views.generic import DetailView
from . import models
from . import utils


class LabelTemplateView(PermissionRequiredMixin, DetailView):
    model = models.Label
    pk_url_kwarg = 'object_id'
    permission_required = 'labels.change_label'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['template'] = self.template
        return data

    def get_object(self, queryset=None):
        self.template = get_object_or_404(models.Template, pk=self.kwargs['template'])
        return super().get_object(queryset=queryset)

    def render_to_response(self, context, **response_kwargs):
        label = context['label']
        file = utils.get_label_pdf(label=label, layout=context['template'].layout)
        response = FileResponse(file, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename={}.pdf'.format(slugify(label.name))
        return response
