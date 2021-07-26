import datetime

from django.shortcuts import render, redirect

from Apart.market_info_app.forms import CreateMarketInfoForm, SearchMarketInfoForm
from Apart.market_info_app.models import MarketInfoModel


def create_market_info(request):
    if request.method == 'GET':
        context = {
            'form': CreateMarketInfoForm()
        }
        return render(request, '', context)
    else:
        form = CreateMarketInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            'form': form
        }
        return render(request, '', context)


def get_filter_values(values):
    key_word = values['key_word'] if 'key_word' in values else ''

    return {
        'key_word': key_word,
    }


def all_market_info(request):
    infos = MarketInfoModel.objects.order_by('published_date').reverse()
    form = SearchMarketInfoForm()

    values = get_filter_values(request.GET)
    key_word = values['key_word']

    if key_word:
        infos = infos.filter(text__icontains=key_word)

    context = {
        'infos': infos,
        'form':form,
    }
    return render(request, 'all_market_info.html', context)




