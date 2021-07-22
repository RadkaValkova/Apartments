from django.contrib import admin

from Apart.market_info_app.models import MarketInfoModel


class MarketInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']
    list_filter = ['published_date']


admin.site.register(MarketInfoModel, MarketInfoAdmin)
