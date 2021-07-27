from django.shortcuts import render, redirect

from Apart.inquiry.forms import InquiryForm, FilterInquiryForm
from Apart.inquiry.models import Inquiry


def create_inquiry(request):
    if request.method == 'GET':
        context = {
            'form': InquiryForm(),
        }
        return render(request, 'inquiries/create_inquiry.html', context)
    else:
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inquiries/inquiry_thanks.html')
        context = {
            'form': form,
        }
        return render(request, 'inquiries/create_inquiry.html', context)


def get_filter_values(values):
    category = values['category'] if 'category' in values else ''
    first_name = values['first_name'] if 'first_name' in values else ''
    last_name = values['last_name'] if 'last_name' in values else ''

    return {
        'category': category,
        'first_name': first_name,
        'last_name': last_name,
    }


def all_inquiries(request):
    inquiries = Inquiry.objects.order_by('id').reverse()
    form = FilterInquiryForm()

    values = get_filter_values(request.GET)
    category = values['category']
    first_name = values['first_name']
    last_name = values['last_name']

    if category:
        inquiries = inquiries.filter(category=category)
    if first_name:
        inquiries = inquiries.filter(first_name__iexact=first_name)
    if last_name:
        inquiries = inquiries.filter(last_name__iexact=last_name)

    context = {
        'inquiries': inquiries,
        'form': form,
    }
    return render(request, 'inquiries/all_inquiries.html', context)
