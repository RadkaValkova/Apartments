from django.test import TestCase, Client
from django.urls import reverse

from Apart.market_info_app.forms import CreateMarketInfoForm
from Tests.base.tests import ApartTestCase


class CreateMarketInfoTests(ApartTestCase):

    def test_getAllMarketInfo_shouldRenderTemplate(self):
        response = self.client.get(reverse('all market info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_market_info.html')

    def test_displayAllMarketInfo_AfterCreate(self):
        data = {
            'title': 'Title',
            'published_date': '2021-07-30',
            'source': 'source',
            'text': 'text',
            'source_url': 'https://source.com'
        }
        new_market_info = CreateMarketInfoForm(data=data)
        self.client.login()
        new_market_info.save()
        response = self.client.get('/marketinfo/')
        self.assertEqual(response.status_code, 200)


