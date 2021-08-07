
from django.urls import reverse

from Apart.inquiry.forms import InquiryForm

from Tests.base.tests import ApartTestCase


class CreateInquiryTests(ApartTestCase):

    def test_getInquiryFormCreate_shouldRenderTemplate(self):
        response = self.client.get(reverse('create inquiry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inquiries/create_inquiry.html')

    def test_displayHomePage_AfterCreate(self):
        data = {
            'category': self.create_category_instance(),
            'first_name': 'Радка',
            'last_name': 'Вълкова',
            'town': 'Пловдив',
            'email': 'radka@abv.bg',
            'phone': '888888',
            'text': 'text',
        }
        new_inquiry = InquiryForm(data=data)
        self.client.login()
        new_inquiry.save()
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)




