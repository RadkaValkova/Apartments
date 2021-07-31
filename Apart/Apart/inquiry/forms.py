from django import forms

from Apart.core.validators import first_upper_letter_validator, is_all_digits_validator
from Apart.inquiry.inquiry_choices import CATEGORY_CHOICES
from Apart.inquiry.models import Inquiry, CategoryModel


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

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES[1:],
        widget=forms.Select(),
    )

    first_name = forms.CharField(
        max_length=15,
        validators=[first_upper_letter_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 15 символа.'}
    )

    last_name = forms.CharField(
        max_length=15,
        validators=[first_upper_letter_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 15 символа.'}
    )

    town = forms.CharField(
        max_length=15,
        validators=[first_upper_letter_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 15 символа.'}
    )

    phone = forms.CharField(
        max_length=20,
        validators=[is_all_digits_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 20 символа'}
    )

    email = forms.EmailField(
        widget=forms.EmailInput()
    )

    text = forms.CharField(
        widget=forms.Textarea(),
        max_length=1000,
        error_messages={'max_length': 'Полето трябва да съдържа до 1000 символа'}
    )


class FilterInquiryForm(BootstrapFormMixin, forms.Form):
    id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput()
    )

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(),
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
