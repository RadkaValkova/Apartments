from Tests.base.tests import ApartTestCase


class ApartmentModelTests(ApartTestCase):

    def test_whenApartmentModel_ExpectSuccess(self):
        # there is not custom validators in the model. test only success
        apartment = self.create_apart(
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

        apartment.full_clean()
        apartment.save()
