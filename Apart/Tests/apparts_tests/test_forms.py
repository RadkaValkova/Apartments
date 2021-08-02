from django.test import TestCase

from Apart.apart_app.forms import CreateApartmentForm
from io import StringIO


class ApartmentModelFormTest(TestCase):
    pass
    # def test_createApartmentFormSave_whenValid(self):
    #     data = {
    #         'type': 'едностаен',
    #         'town': 'Пловдив',
    #         'construction': 'панел',
    #         'construction_year': '2020',
    #         'deal': 'продава',
    #         'status': 'активна обява',
    #         'price_offer': 20000,
    #         # 'price_realized': 0,
    #         'pure_area': 50,
    #         'total_area': 55,
    #         'finishing_works': 'изпълнени',
    #         'furnishing': 'обзаведен',
    #         'description': 'обзаведен апартамент',
    #         'image': 'image.jpg',
    #         'email': 'radka@abv.bg',
    #         'contact_phone': '777 777',
    #     }
    #     form = CreateApartmentForm(data)
    #
    #     self.assertTrue(form.is_valid())

    # def test_notPossibleCreateApartmentForm_whenFormNotValid(self):
    #     data = {
    #         'type': '1',
    #         'town': 'пловдив',
    #         'construction': 'панел',
    #         'construction_year': '2020',
    #         'deal': 'продава',
    #         'status': 'активна обява',
    #         'price_offer': 20000,
    #         # 'price_realized': 0,
    #         'pure_area': 50,
    #         'total_area': 55,
    #         'finishing_works': 'изпълнени',
    #         'furnishing': 'обзаведен',
    #         'description': 'обзаведен апартамент',
    #         'image': 'image.jpg',
    #         'email': 'radka@abv.bg',
    #         'contact_phone': '777 777',
    #     }
    #     form = CreateApartmentForm(data)
    #
    #     self.assertFalse(form.is_valid())




def test_townWhen_StartsLowerCase(self):
    pass


def test_yearWhen_ConstructionYearIsNotAllDigit(self):
    pass
