from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render


def pagination(request, list_of_posts, result_per_page):
    paginator = Paginator(list_of_posts, result_per_page)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return posts
