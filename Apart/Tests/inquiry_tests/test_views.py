from django.test import TestCase, Client
from django.urls import reverse

from Apart.inquiry.forms import InquiryForm
from Apart.inquiry.models import CategoryModel
from Tests.base.tests import ApartTestCase


class CreateInquiryTests(ApartTestCase):

    def test_getInquiryFormCreate_shouldRenderTemplate(self):
        response = self.client.get(reverse('create inquiry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inquiries/create_inquiry.html')




