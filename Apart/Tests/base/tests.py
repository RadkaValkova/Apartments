from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from Apart.apart_app.models import TypeModel, ConstructionModel, DealModel, StatusModel, FinishingWorksModel, \
    FurnishingModel

UserModel = get_user_model()


class ApartTestCase(TestCase):
    logged_in_user_email = 'radka@abv.bg'
    logged_in_user_password = 'parolata123'

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )

    def create_type_instance(self):
        return TypeModel.objects.create(name='Едностаен')

    def create_construction_instance(self):
        return ConstructionModel.objects.create(name='панел')

    def create_deal_instance(self):
        return DealModel.objects.create(name='купува')

    def create_status_instance(self):
        return StatusModel.objects.create(name='активна обява')

    def create_fifnishing_works_instance(self):
        return FinishingWorksModel.objects.create(name='изпълнени')

    def create_furnishing_instance(self):
        return FurnishingModel.objects.create(name='обзаведен')
