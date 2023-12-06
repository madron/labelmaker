import json
from django import forms


class PrettyJSONEncoder(json.JSONEncoder):
    def __init__(self, *args, indent, **kwargs):
        super().__init__(*args, indent=4, **kwargs)


class TemplateForm(forms.ModelForm):
    layout = forms.JSONField(encoder=PrettyJSONEncoder, widget=forms.Textarea(attrs={'rows': 50, 'class': 'input-xxlarge'}))
