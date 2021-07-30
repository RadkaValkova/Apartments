from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from Apart.core.views import get_filter_values
from Apart.market_info_app.forms import CreateMarketInfoForm, SearchMarketInfoForm
from Apart.market_info_app.models import MarketInfoModel


@login_required
def create_market_info(request):
    if request.method == 'GET':
        context = {
            'form': CreateMarketInfoForm()
        }
        return render(request, 'create_market_info.html', context)
    else:
        form = CreateMarketInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all market info')
        context = {
            'form': form
        }
        return render(request, 'create_market_info.html', context)


def all_market_info(request):
    infos = MarketInfoModel.objects.order_by('published_date').reverse()

    values = get_filter_values(request.GET)
    key_word = values['key_word']

    if key_word:
        infos = infos.filter(text__icontains=key_word)

    context = {
        'infos': infos,
        'form': SearchMarketInfoForm(initial=values),
    }
    return render(request, 'all_market_info.html', context)
