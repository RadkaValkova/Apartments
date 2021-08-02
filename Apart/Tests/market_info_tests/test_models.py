from django.test import TestCase

from Apart.market_info_app.models import MarketInfoModel


class MarketInfoModelTests(TestCase):
    valid_title = 'Title'
    valid_published_date = '2021-07-30'
    valid_source = 'source'
    valid_text = 'text'
    valid_source_url = 'https://source.com'

    # there is not custom validators in the model. test only success
    def test_whenMarketInfoModel_ExpectSuccess(self):
        market_info = MarketInfoModel(
            title= self.valid_title,
            published_date=self.valid_published_date,
            source=self.valid_source,
            text=self.valid_text,
            source_url=self.valid_source_url,
        )

        market_info.full_clean()
        market_info.save()

