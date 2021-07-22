from django.urls import path

from Apart.market_info_app.views import create_market_info, all_market_info

urlpatterns = [
    path('', all_market_info, name='all market info')
]