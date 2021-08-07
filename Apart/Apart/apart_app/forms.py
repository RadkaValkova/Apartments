import os

from django import forms
from django.conf import settings

from Apart.apart_app.models import ApartmentModel, TypeModel, ConstructionModel, DealModel, StatusModel, \
    FinishingWorksModel, FurnishingModel
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
        exclude = ('user', 'status', 'price_realized')

    type = forms.ModelChoiceField(
        queryset=TypeModel.objects.all(),
        label='Вид',
    )

    town = forms.CharField(
        max_length=30,
        validators=[first_upper_letter_validator],
        label='Град',
        error_messages={'max_length': 'Полето трябва да съдържа до 30 символа.'}
    )

    construction = forms.ModelChoiceField(
        queryset=ConstructionModel.objects.all(),
        label='Конструкция',
    )

    construction_year = forms.CharField(
        max_length=4,
        validators=[is_all_digits_validator],
        label='Година на построяване',
        error_messages={'max_length': 'Полето трябва да съдържа четири цифри.'}
    )

    deal = forms.ModelChoiceField(
        queryset=DealModel.objects.all(),
        label='Вид на сделката',
    )

    price_offer = forms.IntegerField(
        validators=[positive_value_validator],
        label='Офертна цена в EUR',
    )

    pure_area = forms.IntegerField(
        validators=[positive_value_validator],
        label='Чиста жилищна площ / ЗП',
    )

    total_area = forms.IntegerField(
        validators=[positive_value_validator],
        label='Площ с общи части / РЗП',
    )

    finishing_works = forms.ModelChoiceField(
        queryset=FinishingWorksModel.objects.all(),
        label='Степен на довършителните работи',
    )

    furnishing = forms.ModelChoiceField(
        queryset=FurnishingModel.objects.all(),
        label='Обзавеждане',
    )

    description = forms.CharField(
        widget=forms.Textarea(),
        max_length=1000,
        label='Описание на обекта',
        error_messages={'max_length': 'Полето трябва да съдържа до 1000 символа'}
    )

    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='e-mail',
    )

    contact_phone = forms.CharField(
        max_length=20,
        validators=[is_all_digits_validator],
        label='Телефон за контакт',
        error_messages={'max_length': 'Полето трябва да съдържа до 20 символа'}
    )


class EditApartmentForm(ApartmentForm):

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

    type = forms.ModelChoiceField(
        queryset=TypeModel.objects.all(),
        label='Вид',
    )

    town = forms.CharField(
        max_length=30,
        validators=[first_upper_letter_validator],
        label='Град',
        error_messages={'max_length': 'Полето трябва да съдържа до 30 символа.'}
    )

    construction = forms.ModelChoiceField(
        queryset=ConstructionModel.objects.all(),
        label='Конструкция',
    )

    construction_year = forms.CharField(
        max_length=4,
        validators=[is_all_digits_validator],
        label='Година на построяване',
        error_messages={'max_length': 'Полето трябва да съдържа четири цифри.'}
    )

    deal = forms.ModelChoiceField(
        queryset=DealModel.objects.all(),
        label='Вид на сделката',
    )

    status = forms.ModelChoiceField(
        queryset=StatusModel.objects.all(),
        label='Статус на обявата',
    )

    price_offer = forms.IntegerField(
        validators=[positive_value_validator],
        label='Офертна цена',
    )

    price_realized = forms.IntegerField(
        validators=[positive_value_validator],
        label='Реализирана при сделката цена',
    )


    pure_area = forms.IntegerField(
        validators=[positive_value_validator],
        label='Чиста жилищна площ / ЗП',
    )

    total_area = forms.IntegerField(
        validators=[positive_value_validator],
        label='Площ с общи части / РЗП',
    )

    finishing_works = forms.ModelChoiceField(
        queryset=FinishingWorksModel.objects.all(),
        label='Степен на довършителните работи',
    )

    furnishing = forms.ModelChoiceField(
        queryset=FurnishingModel.objects.all(),
        label='Обзавеждане',
    )

    description = forms.CharField(
        widget=forms.Textarea(),
        max_length=1000,
        label='Описание на обекта',
        error_messages={'max_length': 'Полето трябва да съдържа до 1000 символа'}
    )

    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='e-mail',
    )

    contact_phone = forms.CharField(
        max_length=20,
        validators=[is_all_digits_validator],
        label='Телефон за контакт',
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
