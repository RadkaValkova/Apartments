from django import forms

from Apart.market_info_app.models import MarketInfoModel


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class MarketInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = MarketInfoModel
        fields = '__all__'


class CreateMarketInfoForm(MarketInfoForm):
    pass


# class EditMarketInfoForm(MarketInfoForm):
#     pass
#
#
# class DeleteMarketInfoForm(MarketInfoForm):
#     pass