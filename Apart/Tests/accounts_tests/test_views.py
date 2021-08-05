from django.urls import reverse
from Tests.base.tests import ApartTestCase

from Apart.apart_app.models import ApartmentModel, TypeModel, ConstructionModel, DealModel, StatusModel, \
    FinishingWorksModel, FurnishingModel


class ProfileDetailsTest(ApartTestCase):

    def test_getDetails_whenLoggedInUserWithoutAparts_shouldGetDetailsWithoutAparts(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['aparts']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetails_whenLoggedInUserWithPets_shouldGetDetailsWithPets(self):

        apart = ApartmentModel.objects.create(
            type=TypeModel.objects.first(),
            town='Пловдив',
            construction=ConstructionModel.objects.first(),
            construction_year='2021',
            deal=DealModel.objects.first(),
            status=StatusModel.objects.first(),
            price_offer=20000,
            price_realized=0,
            pure_area=50,
            total_area=50,
            finishing_works=FinishingWorksModel.objects.first(),
            furnishing=FurnishingModel.objects.first(),
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
