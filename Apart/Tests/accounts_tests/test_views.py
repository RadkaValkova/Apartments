from django.urls import reverse

from Apart.accounts.forms import RegisterForm
from Apart.accounts.models import ApartUser
from Tests.base.tests import ApartTestCase

from Apart.apart_app.models import TypeModel, ConstructionModel, DealModel, StatusModel, \
    FinishingWorksModel, FurnishingModel


class ProfileDetailsTest(ApartTestCase):

    def test_getDetails_whenLoggedInUserWithoutAparts_shouldGetDetailsWithoutAparts(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['aparts']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetails_whenLoggedInUserWithAparts_shouldGetDetailsWithAparts(self):
        apart = self.create_apart(
            type=self.create_type_instance(),
            town='Пловдив',
            construction=self.create_construction_instance(),
            construction_year='2021',
            deal=self.create_deal_instance(),
            status=self.create_status_instance(),
            price_offer=20000,
            price_realized=0,
            pure_area=50,
            total_area=50,
            finishing_works=self.create_fifnishing_works_instance(),
            furnishing=self.create_furnishing_instance(),
            description='описание',
            image='image.jpg',
            date='2021-07-30',
            email='radka@abv.bg',
            contact_phone='88888',
            user=self.user,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([apart], list(response.context['aparts']))


