from django.contrib import admin
from django.urls import path
from . import forms
from . import models
from . import views


@admin.register(models.Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'background',)


@admin.register(models.Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def get_urls(self):
        info = dict(app_label=self.model._meta.app_label, model_name=self.model._meta.model_name)
        urls = [
            path('<int:object_id>/template/<slug:template>/',
                self.admin_site.admin_view(views.LabelTemplateView.as_view()),
                name='{app_label}_{model_name}_template'.format(**info)
            ),
        ]
        return urls + super().get_urls()

    def change_view(self, *args, **kwargs):
        kwargs['extra_context'] = kwargs.get('extra_context', dict())
        kwargs['extra_context']['templates'] = [t.name for t in models.Template.objects.order_by('name')]
        return super().change_view(*args, **kwargs)

    def get_actions(self, request):
        actions = super().get_actions(request)
        for template in models.Template.objects.order_by('name'):
            action_func = lambda modeladmin, request, queryset: self.template_action(request, queryset, template)
            action_name = 'template_{}'.format(template.name)
            action_description = 'Template {}'.format(template.name)
            actions[action_name] = (action_func, action_name, action_description)
        return actions

    def template_action(self, request, queryset, template):
        action_name = request.POST['action']
        template_name = action_name.lstrip('template_')
        template = models.Template.objects.get(name=template_name)
        return views.LabelsTemplateView.as_view()(request, queryset=queryset, template=template)


@admin.register(models.Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = forms.TemplateForm
