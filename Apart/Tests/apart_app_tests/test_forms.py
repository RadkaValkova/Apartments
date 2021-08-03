from django.test import TestCase

from Apart.apart_app.forms import CreateApartmentForm
from io import StringIO

from Apart.apart_app.models import TypeModel, ConstructionModel, DealModel, FinishingWorksModel, StatusModel, \
    FurnishingModel


class ApartmentModelFormTest(TestCase):

    # to take foreign keys
    def test_saveApartmentForm_whenValid(self):
        pass
        # TypeModel.objects.create(name='едностаен')
        # ConstructionModel.objects.create(name='панел')
        # DealModel.objects.create(name='купува')
        # StatusModel.objects.create(name='активна обява')
        # FinishingWorksModel.objects.create(name='изпълнени')
        # FurnishingModel.objects.create(name='обзаведен')
        #
        # data = {
        #     'type': TypeModel.objects.get(pk=1).name,  # foreign key
        #     'town': 'Пловдив',
        #     'construction': ConstructionModel.objects.get(pk=1).name,  # foreign key
        #     'construction_year': '2020',
        #     'deal': DealModel.objects.get(pk=1).name,  # foreign key
        #     'status': StatusModel.objects.get(pk=1).name,  # foreign key
        #     'price_offer': 20000,
        #     # 'price_realized': 0,
        #     'pure_area': 50,
        #     'total_area': 55,
        #     'finishing_works': FinishingWorksModel.objects.get(pk=1).name,  # foreign key
        #     'furnishing': FurnishingModel.objects.get(pk=1).name,  # foreign key
        #     'description': 'обзаведен апартамент',
        #     'image': 'image.jpg',
        #     'date': '2021-07-30',
        #     'email': 'radka@abv.bg',
        #     'contact_phone': '777777',
        # }
        #
        # form = CreateApartmentForm(data)
        # self.assertTrue(form.is_valid())
