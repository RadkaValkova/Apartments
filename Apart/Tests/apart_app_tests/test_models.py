from django.test import TestCase, Client

from Apart.accounts.models import ApartUser
from Apart.apart_app.models import ApartmentModel, TypeModel, ConstructionModel, DealModel, StatusModel, \
    FinishingWorksModel, FurnishingModel


class ApartmentModelTests(TestCase):

    def test_whenApartmentModel_ExpectSuccess(self):
        TypeModel.objects.create(name='Едностаен')
        ConstructionModel.objects.create(name='панел')
        DealModel.objects.create(name='купува')
        StatusModel.objects.create(name='активна обява')
        FinishingWorksModel.objects.create(name='изпълнени')
        FurnishingModel.objects.create(name='обзаведен')
        ApartUser.objects.create(email='radka@abv.bg')

        # there is not custom validators in the model. test only success
        apartment = ApartmentModel(
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
            user=ApartUser.objects.first(),
        )

        apartment.full_clean()
        apartment.save()
