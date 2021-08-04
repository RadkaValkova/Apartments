from django.test import TestCase, Client
from django.urls import reverse

from Apart.inquiry.forms import InquiryForm


class CreateInquiryTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getAllInquiries_shouldRenderTemplate(self):
        response = self.test_client.get(reverse('all inquiries'))
        self.assertTemplateUsed(response, 'inquiries/all_inquiries.html')

    def test_getInquiryFormCreate_shouldRenderTemplate(self):
        response = self.test_client.get(reverse('create inquiry'))
        self.assertTemplateUsed(response, 'inquiries/create_inquiry.html')

