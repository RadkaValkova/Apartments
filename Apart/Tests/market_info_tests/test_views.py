from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

from Apart.market_info_app.forms import CreateMarketInfoForm


class CreateMarketInfoTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getAllMarketInfo_shouldRenderTemplate(self):
        response = self.test_client.get(reverse('all market info'))
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
        self.test_client.login()
        new_market_info.save()
        response = self.test_client.get('/marketinfo/')
        self.assertEqual(response.status_code, 200)

    @patch('Apart.market_info_app.models.MarketInfoModel.objects')
    def test_getarketInfo_shouldRenderOrderedObjects(self, marketinfomodel_mock):
        marketinfomodel_mock.order_by('published_date').reverse().return_value = [1]
        response = self.test_client.get(reverse('all market info'))
        self.assertTemplateUsed(response, 'all_market_info.html')
        infos = response.context['infos']
