from django.contrib import admin

from Apart.apart_app.models import TownModel, TypeModel, ApartmentModel, DealModel, StatusModel, ConstructionModel, \
    FurnishingModel, FinishingWorksModel


class ApartAdmin(admin.ModelAdmin):
    list_display = ['type', 'town', 'construction', 'construction_year', 'deal', 'status', 'user']
    list_filter = ['type', 'town', 'date']
    search_fields = ['type', 'town', 'deal', 'status']
    fieldsets = (
        ('Functional information', {
            'fields': (
                'type',
                'town',
                'construction',
                'construction_year',
                'pure_area',
                'total_area',
                'finishing_works',
                'furnishing',
                'description',
                'image',
            )}),
        ('Commercial information', {
            'fields': (
                'price_offer',
                'price_realized',
            )}),
        ('Contact information', {
            'fields': (
                'email',
                'contact_phone',
                'user',
            )}),
    )


admin.site.register(ApartmentModel, ApartAdmin)
admin.site.register(TownModel)
admin.site.register(TypeModel)
admin.site.register(DealModel)
admin.site.register(StatusModel)
admin.site.register(ConstructionModel)
admin.site.register(FurnishingModel)
admin.site.register(FinishingWorksModel)
