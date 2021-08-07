from django.urls import reverse

from Tests.base.tests import ApartTestCase


class CreateMarketInfoTests(ApartTestCase):

    def test_getAllMarketInfo_shouldRenderTemplate(self):
        response = self.client.get(reverse('all market info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_market_info.html')

    def test_createMarketInfoIsPossible_WhenUserIsSuperuser(self):
        self.client.force_login(self.super_user)
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)




