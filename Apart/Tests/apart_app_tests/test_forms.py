from django.test import TestCase

from Apart.apart_app.forms import CreateApartmentForm
from Apart.apart_app.models import TypeModel, ConstructionModel, DealModel, FinishingWorksModel, StatusModel, \
    FurnishingModel

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class ApartmentModelFormTest(TestCase):
    im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
    im_io = BytesIO()  # a BytesIO object for saving image
    im.save(im_io, 'JPEG')  # save the image to im_io
    im_io.seek(0)  # seek to the beginning
    image = InMemoryUploadedFile(im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None)

    def test_saveCreateApartmentForm_whenValid(self):
        TypeModel.objects.create(name='Едностаен')
        ConstructionModel.objects.create(name='панел')
        DealModel.objects.create(name='купува')
        StatusModel.objects.create(name='активна обява')
        FinishingWorksModel.objects.create(name='изпълнени')
        FurnishingModel.objects.create(name='обзаведен')

        data = {
            'type': TypeModel.objects.get(pk=1),
            'town': 'Пловдив',
            'construction': ConstructionModel.objects.get(pk=1),
            'construction_year': '2020',
            'deal': DealModel.objects.get(pk=1),
            'status': StatusModel.objects.get(pk=1),
            'price_offer': 20000,
            'pure_area': 50,
            'total_area': 55,
            'finishing_works': FinishingWorksModel.objects.get(pk=1),
            'furnishing': FurnishingModel.objects.get(pk=1),
            'description': 'обзаведен апартамент',
            'email': 'radka@abv.bg',
            'contact_phone': '777777',
        }
        file_dict = {'image': self.image}

        form = CreateApartmentForm(data=data, files=file_dict)
        self.assertTrue(form.is_valid(), form.errors)

    # def test_saveApartmentForm_townInvalidStartsLowerCase(self):
    #     TypeModel.objects.create(name='Едностаен')
    #     ConstructionModel.objects.create(name='панел')
    #     DealModel.objects.create(name='купува')
    #     StatusModel.objects.create(name='активна обява')
    #     FinishingWorksModel.objects.create(name='изпълнени')
    #     FurnishingModel.objects.create(name='обзаведен')
    #
    #     data = {
    #         'type': TypeModel.objects.get(pk=1),
    #         'town': 'пловдив',
    #         'construction': ConstructionModel.objects.get(pk=1),
    #         'construction_year': '2020',
    #         'deal': DealModel.objects.get(pk=1),
    #         'status': StatusModel.objects.get(pk=1),
    #         'price_offer': 20000,
    #         'pure_area': 50,
    #         'total_area': 55,
    #         'finishing_works': FinishingWorksModel.objects.get(pk=1),
    #         'furnishing': FurnishingModel.objects.get(pk=1),
    #         'description': 'обзаведен апартамент',
    #
    #         'email': 'radka@abv.bg',
    #         'contact_phone': '777777',
    #     }
    #     file_dict = {'image': self.image}
    #     form = CreateApartmentForm(data=data, files=file_dict)
    #     self.assertFalse(form.is_valid())

    # def test_saveApartmentForm_constructionYearInvalidNotAllDigit(self):
    #     TypeModel.objects.create(name='Едностаен')
    #     ConstructionModel.objects.create(name='панел')
    #     DealModel.objects.create(name='купува')
    #     StatusModel.objects.create(name='активна обява')
    #     FinishingWorksModel.objects.create(name='изпълнени')
    #     FurnishingModel.objects.create(name='обзаведен')
    #
    #     data = {
    #         'type': TypeModel.objects.get(pk=1),
    #         'town': 'Пловдив',
    #         'construction': ConstructionModel.objects.get(pk=1),
    #         'construction_year': 'нннн',
    #         'deal': DealModel.objects.get(pk=1),
    #         'status': StatusModel.objects.get(pk=1),
    #         'price_offer': 20000,
    #         'pure_area': 50,
    #         'total_area': 55,
    #         'finishing_works': FinishingWorksModel.objects.get(pk=1),
    #         'furnishing': FurnishingModel.objects.get(pk=1),
    #         'description': 'обзаведен апартамент',
    #         'image': 'image.jpg',
    #         'email': 'radka@abv.bg',
    #         'contact_phone': '777777',
    #     }
    #     file_dict = {'image': self.image}
    #     form = CreateApartmentForm(data=data, files=file_dict)
    #     self.assertFalse(form.is_valid())
    #
    # def test_saveApartmentForm_priceOfferInvalidNotPositive(self):
    #     TypeModel.objects.create(name='Едностаен')
    #     ConstructionModel.objects.create(name='панел')
    #     DealModel.objects.create(name='купува')
    #     StatusModel.objects.create(name='активна обява')
    #     FinishingWorksModel.objects.create(name='изпълнени')
    #     FurnishingModel.objects.create(name='обзаведен')
    #
    #     data = {
    #         'type': TypeModel.objects.get(pk=1),
    #         'town': 'Пловдив',
    #         'construction': ConstructionModel.objects.get(pk=1),
    #         'construction_year': '2020',
    #         'deal': DealModel.objects.get(pk=1),
    #         'status': StatusModel.objects.get(pk=1),
    #         'price_offer': -5,
    #         'pure_area': 50,
    #         'total_area': 55,
    #         'finishing_works': FinishingWorksModel.objects.get(pk=1),
    #         'furnishing': FurnishingModel.objects.get(pk=1),
    #         'description': 'обзаведен апартамент',
    #         'image': 'image.jpg',
    #         'email': 'radka@abv.bg',
    #         'contact_phone': '777777',
    #     }
    #
    #     file_dict = {'image': self.image}
    #     form = CreateApartmentForm(data=data, files=file_dict)
    #     self.assertFalse(form.is_valid())
    #
    # def test_saveApartmentForm_pureAreaInvalidNotPositive(self):
    #     TypeModel.objects.create(name='Едностаен')
    #     ConstructionModel.objects.create(name='панел')
    #     DealModel.objects.create(name='купува')
    #     StatusModel.objects.create(name='активна обява')
    #     FinishingWorksModel.objects.create(name='изпълнени')
    #     FurnishingModel.objects.create(name='обзаведен')
    #
    #     data = {
    #         'type': TypeModel.objects.get(pk=1),
    #         'town': 'Пловдив',
    #         'construction': ConstructionModel.objects.get(pk=1),
    #         'construction_year': '2020',
    #         'deal': DealModel.objects.get(pk=1),
    #         'status': StatusModel.objects.get(pk=1),
    #         'price_offer': 20000,
    #         'pure_area': -5,
    #         'total_area': 55,
    #         'finishing_works': FinishingWorksModel.objects.get(pk=1),
    #         'furnishing': FurnishingModel.objects.get(pk=1),
    #         'description': 'обзаведен апартамент',
    #         'image': 'image.jpg',
    #         'email': 'radka@abv.bg',
    #         'contact_phone': '777777',
    #     }
    #
    #     file_dict = {'image': self.image}
    #     form = CreateApartmentForm(data=data, files=file_dict)
    #     self.assertFalse(form.is_valid())
    #
    # def test_saveApartmentForm_totalAreaInvalidNotPositive(self):
    #     TypeModel.objects.create(name='Едностаен')
    #     ConstructionModel.objects.create(name='панел')
    #     DealModel.objects.create(name='купува')
    #     StatusModel.objects.create(name='активна обява')
    #     FinishingWorksModel.objects.create(name='изпълнени')
    #     FurnishingModel.objects.create(name='обзаведен')
    #
    #     data = {
    #         'type': TypeModel.objects.get(pk=1),
    #         'town': 'Пловдив',
    #         'construction': ConstructionModel.objects.get(pk=1),
    #         'construction_year': '2020',
    #         'deal': DealModel.objects.get(pk=1),
    #         'status': StatusModel.objects.get(pk=1),
    #         'price_offer': 20000,
    #         'pure_area': 50,
    #         'total_area': -5,
    #         'finishing_works': FinishingWorksModel.objects.get(pk=1),
    #         'furnishing': FurnishingModel.objects.get(pk=1),
    #         'description': 'обзаведен апартамент',
    #         'image': 'image.jpg',
    #         'email': 'radka@abv.bg',
    #         'contact_phone': '777777',
    #     }
    #
    #     file_dict = {'image': self.image}
    #     form = CreateApartmentForm(data=data, files=file_dict)
    #     self.assertFalse(form.is_valid())
    #
    # def test_saveApartmentForm_contactPhoneInvalidNotAllDigit(self):
    #     TypeModel.objects.create(name='Едностаен')
    #     ConstructionModel.objects.create(name='панел')
    #     DealModel.objects.create(name='купува')
    #     StatusModel.objects.create(name='активна обява')
    #     FinishingWorksModel.objects.create(name='изпълнени')
    #     FurnishingModel.objects.create(name='обзаведен')
    #
    #     data = {
    #         'type': TypeModel.objects.get(pk=1),
    #         'town': 'Пловдив',
    #         'construction': ConstructionModel.objects.get(pk=1),
    #         'construction_year': '2020',
    #         'deal': DealModel.objects.get(pk=1),
    #         'status': StatusModel.objects.get(pk=1),
    #         'price_offer': 20000,
    #         'pure_area': 50,
    #         'total_area': 55,
    #         'finishing_works': FinishingWorksModel.objects.get(pk=1),
    #         'furnishing': FurnishingModel.objects.get(pk=1),
    #         'description': 'обзаведен апартамент',
    #         'image': 'image.jpg',
    #         'email': 'radka@abv.bg',
    #         'contact_phone': 'fffff',
    #     }
    #
    #     file_dict = {'image': self.image}
    #     form = CreateApartmentForm(data=data, files=file_dict)
    #     self.assertFalse(form.is_valid())