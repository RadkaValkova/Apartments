from django.shortcuts import render, redirect


from Apart.inquiry.forms import InquiryForm
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


def all_inquiries(request):
    all_inquiries = Inquiry.objects.order_by('id').reverse()
    context = {
        'inquiries': all_inquiries,
    }
    return render(request, 'inquiries/all_inquiries.html', context)



