from django.core.paginator import Paginator
from django.shortcuts import render


def pagination(request, list_obj):
    paginator = Paginator(list_obj, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_filter_values(values):
    category = values['category'] if 'category' in values else ''
    first_name = values['first_name'] if 'first_name' in values else ''
    last_name = values['last_name'] if 'last_name' in values else ''
    key_word = values['key_word'] if 'key_word' in values else ''
    town = values['town'] if 'town' in values else ''
    type = values['type'] if 'type' in values else ''
    construction = values['construction'] if 'construction' in values else ''
    deal = values['deal'] if 'deal' in values else ''

    return {
        'category': category,
        'first_name': first_name,
        'last_name': last_name,
        'key_word': key_word,
        'town': town,
        'type': type,
        'construction': construction,
        'deal': deal,
    }



