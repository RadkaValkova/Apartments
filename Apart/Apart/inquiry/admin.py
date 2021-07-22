from django.contrib import admin

from Apart.inquiry.models import Inquiry, CategoryModel


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['category', 'date', 'first_name', 'last_name', 'phone']
    list_filter = ['category', 'date']


admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(CategoryModel)
