from django.test import TestCase, Client
from django.urls import reverse

from Tests.base.tests import ApartTestCase


class CreateInquiryTests(ApartTestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getInquiryFormCreate_shouldRenderTemplate(self):
        response = self.test_client.get(reverse('create inquiry'))
        self.assertTemplateUsed(response, 'inquiries/create_inquiry.html')



