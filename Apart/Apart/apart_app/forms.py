import os
from os.path import join

from django import forms
from django.conf import settings

from Apart.apart_app.apart_choices import TYPE_CHOICES
from Apart.apart_app.models import ApartmentModel, TownModel, TypeModel, ConstructionModel, DealModel
from Apart.apart_app.validators import positive_value_validator


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

        town = forms.CharField(
            widget=forms.TextInput(
                attrs={'placeholder': 'въведете град'}
            ),
            help_text='моля въведете град',
            validators=[]
        )

    def clean_town(self):
        return self.cleaned_data['town'].capitalize()


class CreateApartmentForm(ApartmentForm):
    pass


class EditApartmentForm(ApartmentForm):
    def save(self, commit=True):
        db_apart = ApartmentModel.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_apart.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = ApartmentModel
        exclude = ('user',)
        fields = '__all__'


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

