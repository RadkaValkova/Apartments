import tempfile

from Apart.apart_app.forms import CreateApartmentForm

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from Tests.base.tests import ApartTestCase


class ApartmentModelFormTest(ApartTestCase):
    im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
    im_io = BytesIO()  # a BytesIO object for saving image
    im.save(im_io, 'JPEG')  # save the image to im_io
    im_io.seek(0)  # seek to the beginning
    image = InMemoryUploadedFile(im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None)

    def test_saveCreateApartmentForm_whenValid(self):
        data = {
            'type': self.create_type_instance(),
            'town': 'Пловдив',
            'construction': self.create_construction_instance(),
            'construction_year': '2020',
            'deal': self.create_deal_instance(),
            'status': self.create_status_instance(),
            'price_offer': 20000,
            'pure_area': 50,
            'total_area': 55,
            'finishing_works': self.create_fifnishing_works_instance(),
            'furnishing': self.create_furnishing_instance(),
            'description': 'обзаведен апартамент',
            'email': 'radka@abv.bg',
            'contact_phone': '777777',
        }
        # file_dict = {'file': tempfile.NamedTemporaryFile(suffix="_test.jpg").name,}
        file_dict = {'image': self.image}

        form = CreateApartmentForm(data=data, files=file_dict)
        self.assertTrue(form.is_valid(), form.errors)

    def test_saveApartmentForm_townInvalidStartsLowerCase(self):
        data = {
            'type': self.create_type_instance(),
            'town': 'пловдив',
            'construction': self.create_construction_instance(),
            'construction_year': '2020',
            'deal': self.create_deal_instance(),
            'status': self.create_status_instance(),
            'price_offer': 20000,
            'pure_area': 50,
            'total_area': 55,
            'finishing_works': self.create_fifnishing_works_instance(),
            'furnishing': self.create_furnishing_instance(),
            'description': 'обзаведен апартамент',

            'email': 'radka@abv.bg',
            'contact_phone': '777777',
        }
        file_dict = {'image': self.image}
        form = CreateApartmentForm(data=data, files=file_dict)
        self.assertEqual(form.errors['town'], ['Изпишете името с главна буква'])
        self.assertFalse(form.is_valid())

    def test_saveApartmentForm_constructionYearInvalidNotAllDigit(self):
        data = {
            'type': self.create_type_instance(),
            'town': 'Пловдив',
            'construction': self.create_construction_instance(),
            'construction_year': 'нннн',
            'deal': self.create_deal_instance(),
            'status': self.create_status_instance(),
            'price_offer': 20000,
            'pure_area': 50,
            'total_area': 55,
            'finishing_works': self.create_fifnishing_works_instance(),
            'furnishing': self.create_furnishing_instance(),
            'description': 'обзаведен апартамент',
            'image': 'image.jpg',
            'email': 'radka@abv.bg',
            'contact_phone': '777777',
        }
        file_dict = {'image': self.image}
        form = CreateApartmentForm(data=data, files=file_dict)
        self.assertEqual(form.errors['construction_year'], ['Полето може да съдържа само цифри'])
        self.assertFalse(form.is_valid())

    def test_saveApartmentForm_priceOfferInvalidNotPositive(self):
        data = {
            'type': self.create_type_instance(),
            'town': 'Пловдив',
            'construction': self.create_construction_instance(),
            'construction_year': '2020',
            'deal': self.create_deal_instance(),
            'status': self.create_status_instance(),
            'price_offer': -5,
            'pure_area': 50,
            'total_area': 55,
            'finishing_works': self.create_fifnishing_works_instance(),
            'furnishing': self.create_furnishing_instance(),
            'description': 'обзаведен апартамент',
            'image': 'image.jpg',
            'email': 'radka@abv.bg',
            'contact_phone': '777777',
        }

        file_dict = {'image': self.image}
        form = CreateApartmentForm(data=data, files=file_dict)
        self.assertEqual(form.errors['price_offer'], ['Моля, попълнете стойност по-голяма от нула'])
        self.assertFalse(form.is_valid())

    def test_saveApartmentForm_pureAreaInvalidNotPositive(self):
        data = {
            'type': self.create_type_instance(),
            'town': 'Пловдив',
            'construction': self.create_construction_instance(),
            'construction_year': '2020',
            'deal': self.create_deal_instance(),
            'status': self.create_status_instance(),
            'price_offer': 20000,
            'pure_area': -5,
            'total_area': 55,
            'finishing_works': self.create_fifnishing_works_instance(),
            'furnishing': self.create_furnishing_instance(),
            'description': 'обзаведен апартамент',
            'image': 'image.jpg',
            'email': 'radka@abv.bg',
            'contact_phone': '777777',
        }

        file_dict = {'image': self.image}
        form = CreateApartmentForm(data=data, files=file_dict)
        self.assertEqual(form.errors['pure_area'], ['Моля, попълнете стойност по-голяма от нула'])
        self.assertFalse(form.is_valid())

    def test_saveApartmentForm_totalAreaInvalidNotPositive(self):
        data = {
            'type': self.create_type_instance(),
            'town': 'Пловдив',
            'construction': self.create_construction_instance(),
            'construction_year': '2020',
            'deal': self.create_deal_instance(),
            'status': self.create_status_instance(),
            'price_offer': 20000,
            'pure_area': 50,
            'total_area': -5,
            'finishing_works': self.create_fifnishing_works_instance(),
            'furnishing': self.create_furnishing_instance(),
            'description': 'обзаведен апартамент',
            'image': 'image.jpg',
            'email': 'radka@abv.bg',
            'contact_phone': '777777',
        }

        file_dict = {'image': self.image}
        form = CreateApartmentForm(data=data, files=file_dict)
        self.assertEqual(form.errors['total_area'], ['Моля, попълнете стойност по-голяма от нула'])
        self.assertFalse(form.is_valid())

    def test_saveApartmentForm_contactPhoneInvalidNotAllDigit(self):
        data = {
            'type': self.create_type_instance(),
            'town': 'Пловдив',
            'construction': self.create_construction_instance(),
            'construction_year': '2020',
            'deal': self.create_deal_instance(),
            'status': self.create_status_instance(),
            'price_offer': 20000,
            'pure_area': 50,
            'total_area': 55,
            'finishing_works': self.create_fifnishing_works_instance(),
            'furnishing': self.create_furnishing_instance(),
            'description': 'обзаведен апартамент',
            'image': 'image.jpg',
            'email': 'radka@abv.bg',
            'contact_phone': 'fffff',
        }

        file_dict = {'image': self.image}
        form = CreateApartmentForm(data=data, files=file_dict)
        self.assertEqual(form.errors['contact_phone'], ['Полето може да съдържа само цифри'])
        self.assertFalse(form.is_valid())
