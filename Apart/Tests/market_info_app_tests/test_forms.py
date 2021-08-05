from django.test import TestCase

from Apart.market_info_app.forms import CreateMarketInfoForm


class CreateMarketInfoFormTests(TestCase):

    def test_saveMarketInfoForm_whenValid(self):
        data = {
            'title': 'Title',
            'published_date': '2021-07-30',
            'source': 'source',
            'text': 'text',
            'source_url': 'https://source.com'
        }

        form = CreateMarketInfoForm(data=data)
        self.assertTrue(form.is_valid())

    # all other validations are built in
    def test_saveMarketInfoFormNotPossible_whenInvalidTitle_startsLowerCase(self):
        data = {
            'title': 'title',
            'published_date': '2020-12-30',
            'source': 'source',
            'text': 'text',
            'source_url': 'https://source.com'
        }

        form = CreateMarketInfoForm(data=data)
        self.assertFalse(form.is_valid())