from django.test import TestCase

from Apart.inquiry.forms import InquiryForm
from Apart.inquiry.models import Inquiry


class CreateInquiryFormTests(TestCase):
    pass
    # def test_saveInquiryForm_whenValid(self):
    #
    #     category = None
    #     data = {
    #         'first_name': 'Радка',
    #         'last_name': 'Вълкова',
    #         'town': 'Пловдив',
    #         'email': 'radka@abv.bg',
    #         'phone': '888 888',
    #         'category': category,
    #         # 'date': '2021-07-30',
    #         'text': 'text',
    #     }
    #
    #     form = InquiryForm(data=data)
    #     self.assertTrue(form.is_valid())