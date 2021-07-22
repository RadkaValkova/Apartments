from django import forms
from django.core.exceptions import ValidationError

from Apart.inquiry.models import Inquiry
from django.utils.translation import ugettext_lazy as _


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class InquiryForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Inquiry
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].capitalize()

    def clean_town(self):
        return self.cleaned_data['town'].capitalize()

