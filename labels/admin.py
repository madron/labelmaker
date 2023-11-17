from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext as _
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


@admin.register(models.Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)
