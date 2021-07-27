from django import forms
from django.core.exceptions import ValidationError

from Apart.core.validators import max_length_validator
from Apart.inquiry.models import Inquiry, CategoryModel
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
        data = self.cleaned_data['first_name']
        if data[0].islower():
            raise ValidationError('Изпишете името с главна буква')
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if data[0].islower():
            raise ValidationError('Изпишете фамилията с главна буква')
        return data

    def clean_town(self):
        data = self.cleaned_data['town']
        if data[0].islower():
            raise ValidationError('Изпишете градът с главна буква')
        return data


class FilterInquiryForm(BootstrapFormMixin, forms.Form):
    id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput()
    )

    category = forms.ModelChoiceField(
        queryset=CategoryModel.objects.all(),
        required=False,
        label='Категория',
        help_text='Филтър по категория на запитването',
    )
    first_name = forms.CharField(
        max_length=15,
        required=False,
        label='Име',
        help_text='Филтър по име.',
    )
    last_name = forms.CharField(
        max_length=15,
        required=False,
        label='Фамилия',
        help_text='Филтър по фамилия.',
    )
