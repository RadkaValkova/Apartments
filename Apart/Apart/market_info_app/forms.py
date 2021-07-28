from django import forms

from Apart.core.validators import first_upper_letter_validator
from Apart.market_info_app.models import MarketInfoModel


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class MarketInfoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = MarketInfoModel
        fields = '__all__'


class CreateMarketInfoForm(MarketInfoForm):
    title = forms.CharField(
        max_length=15,
        validators=[first_upper_letter_validator],
        error_messages={'max_length': 'Полето трябва да съдържа до 15 символа.'}
    )

    source = forms.CharField(
        max_length=50,
        error_messages={'max_length': 'Полето трябва да съдържа до 15 символа.'}
    )

    text = forms.CharField(
        widget=forms.Textarea(),
        max_length=1000,
        error_messages={'max_length': 'Полето трябва да съдържа до 1000 символа'}
    )

    published_date = forms.DateField(
        widget=forms.DateInput(
            format=('%m/%d/%Y'),
            attrs={'type': 'date'}
        )
    )


# class EditMarketInfoForm(MarketInfoForm):
#     pass
#
#
# class DeleteMarketInfoForm(MarketInfoForm):
#     pass


class SearchMarketInfoForm(forms.Form):
    id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput()
    )
    key_word = forms.CharField(
        max_length=30,
        required=False,
        label='Ключова дума',
        help_text='Моля, попълнете ключова дума, по която да потърсите публикация.',
    )
