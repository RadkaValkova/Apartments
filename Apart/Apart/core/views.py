from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render


def pagination(request, list_obj):
    paginator = Paginator(list_obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj



