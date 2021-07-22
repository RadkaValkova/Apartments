from django.shortcuts import render, redirect

from Apart.market_info_app.forms import CreateMarketInfoForm
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


def all_market_info(request):
    infos = MarketInfoModel.objects.all()
    context = {
        'infos': infos,
    }
    return render(request, 'all_market_info.html', context)