from django.urls import path

from Apart.inquiry.views import create_inquiry, all_inquiries

urlpatterns = [
    path('', create_inquiry, name='create inquiry'),
    path('all/', all_inquiries, name='all inquiries'),
]