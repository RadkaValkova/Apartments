from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render


# def pagination(request, list_of_posts, result_per_page):
#     paginator = Paginator(list_of_posts, result_per_page)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#     try:
#         posts = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         posts = paginator.page(paginator.num_pages)
#
#     return posts

def pagination(request, list_obj):
    paginator = Paginator(list_obj, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj



