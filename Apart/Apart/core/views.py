from django.core.paginator import Paginator
from django.shortcuts import render


def pagination(request, list_obj):
    paginator = Paginator(list_obj, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_filter_values(values):
    # search fields in inquiry
    category = values['category'] if 'category' in values else ''
    first_name = values['first_name'] if 'first_name' in values else None
    last_name = values['last_name'] if 'last_name' in values else None

    # search fields in market info
    key_word = values['key_word'] if 'key_word' in values else None

    # search fields in all aparts
    town = values['town'] if 'town' in values else None
    type = values['type'] if 'type' in values else None
    construction = values['construction'] if 'construction' in values else None
    deal = values['deal'] if 'deal' in values else None

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



