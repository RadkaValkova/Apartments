import os
from os.path import join

from django import forms
from django.conf import settings

from Apart.apart_app.models import ApartmentModel, TypeModel, ConstructionModel, DealModel
from Apart.core.validators import first_upper_letter_validator, positive_value_validator, is_all_digits_validator


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class ApartmentForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = ApartmentModel
        exclude = ('user',)


class CreateApartmentForm(ApartmentForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = ApartmentModel
        exclude = ('user',)

    town = forms.CharField(
        max_length=30,
        validators=[first_upper_letter_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 30 символа.'}
    )

    construction_year = forms.CharField(
        max_length=4,
        validators=[is_all_digits_validator],
        error_messages={'max_length': 'Полето трябва да съдържа четири цифри.'}
    )

    price_offer = forms.IntegerField(
        validators=[positive_value_validator]
    )

    price_realized = forms.IntegerField(
        required=False,
        validators=[positive_value_validator]
    )

    pure_area = forms.IntegerField(
        validators=[positive_value_validator]
    )

    total_area = forms.IntegerField(
        validators=[positive_value_validator]
    )

    description = forms.CharField(
        widget=forms.Textarea(),
        max_length=1000,
        error_messages={'max_length': 'Полето трябва да съдържа до 1000 символа'}
    )

    contact_phone = forms.CharField(
        max_length=20,
        validators=[is_all_digits_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 20 символа'}
    )


class EditApartmentForm(ApartmentForm):
    # def save(self, commit=True):
    #     db_apart = ApartmentModel.objects.get(pk=self.instance.id)
    #     if commit:
    #         image_path = join(settings.MEDIA_ROOT, str(db_apart.image))
    #         os.remove(image_path)
    #     return super().save(commit)

    def save(self, commit=True):
        db_apart = ApartmentModel.objects.get(pk=self.instance.pk)
        new_image = self.files.get('image')
        old_image = str(db_apart.image)
        old_image_path = os.path.join(settings.MEDIA_ROOT,old_image)
        if commit and new_image and old_image:
            os.remove(old_image_path)
        return super().save(commit=commit)

    class Meta:
        model = ApartmentModel
        exclude = ('user',)
        fields = '__all__'

    town = forms.CharField(
        max_length=30,
        validators=[first_upper_letter_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 30 символа.'}
    )

    construction_year = forms.CharField(
        max_length=4,
        validators=[is_all_digits_validator],
        error_messages={'max_length': 'Полето трябва да съдържа четири цифри.'}
    )

    price_offer = forms.IntegerField(
        validators=[positive_value_validator]
    )

    price_realized = forms.IntegerField(
        required=False,
        validators=[positive_value_validator]
    )

    pure_area = forms.IntegerField(
        validators=[positive_value_validator]
    )

    total_area = forms.IntegerField(
        validators=[positive_value_validator]
    )

    description = forms.CharField(
        widget=forms.Textarea(),
        max_length=1000,
        error_messages={'max_length': 'Полето трябва да съдържа до 1000 символа'}
    )

    email = forms.EmailField(
        widget=forms.EmailInput()
    )

    contact_phone = forms.CharField(
        max_length=20,
        validators=[is_all_digits_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 20 символа'}
    )


class FilterApartsForm(BootstrapFormMixin, forms.Form):
    id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput()
    )
    town = forms.CharField(
        max_length=30,
        required=False,
        label='Град',
        help_text='Моля, попълнете град, в който търсите имот.'
    )
    type = forms.ModelChoiceField(
        queryset=TypeModel.objects.all(),
        required=False,
        label='Вид',
        help_text='Моля, изберете от падащото меню, вид на имота, който търсите.'
    )
    construction = forms.ModelChoiceField(
        queryset=ConstructionModel.objects.all(),
        required=False,
        label='Конструкция',
        help_text='Моля, изберете от падащото меню, тип конструкция.'
    )
    deal = forms.ModelChoiceField(
        queryset=DealModel.objects.all(),
        required=False,
        label='Вид сделка',
        help_text='Моля, изберете от падащото меню видът на сделката.'
    )
