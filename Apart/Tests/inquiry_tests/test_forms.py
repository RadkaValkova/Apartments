from django.test import TestCase

from Apart.inquiry.forms import InquiryForm


class CreateInquiryFormTests(TestCase):

    def test_saveInquiryForm_whenValid(self):
        data = {
            'category': 'друго',
            'first_name': 'Радка',
            'last_name': 'Вълкова',
            'town': 'Пловдив',
            'email': 'radka@abv.bg',
            'phone': '888888',
            'text': 'text',
        }

        form = InquiryForm(data=data)
        self.assertTrue(form.is_valid())

        # tests only cases and fields with custom validation

    def test_saveInquiryForm_FirstNameInvalidStartsLowerCase(self):
        data = {
            'category': 'друго',
            'first_name': 'радка',
            'last_name': 'Вълкова',
            'town': 'Пловдив',
            'email': 'radka@abv.bg',
            'phone': '888888',
            'text': 'text',
        }

        form = InquiryForm(data=data)
        self.assertFalse(form.is_valid())

    def test_saveInquiryForm_LastNameInvalidStartsLowerCase(self):
        data = {
            'category': 'друго',
            'first_name': 'Радка',
            'last_name': 'вълкова',
            'town': 'Пловдив',
            'email': 'radka@abv.bg',
            'phone': '888888',
            'text': 'text',
        }

        form = InquiryForm(data=data)
        self.assertFalse(form.is_valid())

    def test_saveInquiryForm_TownInvalidStartsLowerCase(self):
        data = {
            'category': 'друго',
            'first_name': 'Радка',
            'last_name': 'Вълкова',
            'town': 'пловдив',
            'email': 'radka@abv.bg',
            'phone': '888888',
            'text': 'text',
        }

        form = InquiryForm(data=data)
        self.assertFalse(form.is_valid())

    def test_saveInquiryForm_PhoneInvalidNotIsAllDigits(self):
        data = {
            'category': 'друго',
            'first_name': 'Радка',
            'last_name': 'Вълкова',
            'town': 'Пловдив',
            'email': 'radka@abv.bg',
            'phone': 'дддддд',
            'text': 'text',
        }

        form = InquiryForm(data=data)
        self.assertFalse(form.is_valid())
