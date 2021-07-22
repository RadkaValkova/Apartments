from django import forms

from Apart.apart_app.apart_choices import TYPE_CHOICES
from Apart.apart_app.models import ApartmentModel, TypeModel
from Apart.apart_app.validators import positive_value_validator
from django.utils.translation import gettext_lazy as _


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
        fields = '__all__'

        error_messages = {
            'construction_year': {
                'max_length': _("Годината на построяване е с невалидна стойност"),
            },
        }

    # construction_year = forms.CharField(max_length=4)
    #
    # price_offer = forms.IntegerField(
    #     validators=[positive_value_validator],
    # )
    #
    # pure_area = forms.IntegerField(
    #     validators=[positive_value_validator],
    # )
    #
    # total_area = forms.IntegerField(
    #     validators=[positive_value_validator],
    # )
    #
    # description = forms.CharField(
    #     widget=forms.Textarea(),
    # )
    #
    # email = forms.EmailField(
    #     widget=forms.EmailInput(),
    # )

    def clean_town(self):
        return self.cleaned_data['town'].capitalize()


class CreateApartmentForm(ApartmentForm):
    pass


class EditApartmentForm(ApartmentForm):
    pass
    # def save(self, commit=True):
    #     db_apart = ApartmentModel.objects.get(pk=self.instance.id)
    #     if commit:
    #         image_path = join(settings.MEDIA_ROOT, str(db_apart.image))
    #         os.remove(image_path)
    #     return super().save(commit)

    # class Meta:
    #     model = ApartmentModel
    #     fields = '__all__'


class FilterApartsForm(forms.Form):
    town = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'град'}),
        required=False,
    )

    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'вид'}),
        required=False,
    )

