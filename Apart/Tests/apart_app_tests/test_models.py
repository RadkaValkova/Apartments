from django.test import TestCase, Client

from Apart.accounts.models import ApartUser
from Apart.apart_app.models import ApartmentModel, TypeModel, ConstructionModel, DealModel, StatusModel, \
    FinishingWorksModel, FurnishingModel


class ApartmentModelTests(TestCase):
    pass
    # valid_type = TypeModel.objects.get(pk=1)
    # valid_town = 'Пловдив'
    # valid_construction = ConstructionModel.objects.get(pk=1)
    # valid_construction_year = '2021'
    # valid_deal = DealModel.objects.get(pk=1)
    # valid_status = StatusModel.objects.get(pk=1)
    # valid_price_offer = 20000
    # valid_price_realized = 0
    # valid_pure_area = 50
    # valid_total_area = 55
    # valid_finishing_works = FinishingWorksModel.objects.get(pk=1)
    # valid_furnishing = FurnishingModel.objects.get(pk=1)
    # valid_description = 'описание'
    # valid_image = 'image.jpg'
    # valid_date = '2021-07-30'
    # valid_email = 'radka@abv.bg'
    # valid_contact_phone = '888888'
    # valid_user = ApartUser.objects.get(pk=1)
    #
    # def test_whenApartmentModel_ExpectSuccess(self):
    #     apartment = ApartmentModel(
    #         type=self.valid_type,
    #         town=self.valid_town,
    #         construction=self.valid_construction,
    #         construction_year=self.valid_construction_year,
    #         deal=self.valid_deal,
    #         status=self.valid_status,
    #         price_offer=self.valid_price_offer,
    #         price_realized=self.valid_price_realized,
    #         pure_area=self.valid_pure_area,
    #         total_area=self.valid_total_area,
    #         finishing_works=self.valid_finishing_works,
    #         furnishing=self.valid_furnishing,
    #         description=self.valid_description,
    #         image=self.valid_image,
    #         date=self.valid_date,
    #         email=self.valid_email,
    #         contact_phone=self.valid_contact_phone,
    #         user=self.valid_user,
    #     )
    #
    #     apartment.full_clean()
    #     apartment.save()
