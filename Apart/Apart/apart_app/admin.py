from django.contrib import admin

from Apart.apart_app.models import TownModel, TypeModel, ApartmentModel, DealModel, StatusModel, ConstructionModel, \
    FurnishingModel, FinishingWorksModel


class ApartAdmin(admin.ModelAdmin):
    pass



admin.site.register(ApartmentModel, ApartAdmin)

admin.site.register(TownModel)
admin.site.register(TypeModel)
admin.site.register(DealModel)
admin.site.register(StatusModel)
admin.site.register(ConstructionModel)
admin.site.register(FurnishingModel)
admin.site.register(FinishingWorksModel)
