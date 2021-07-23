from django.contrib import admin

from Apart.inquiry.models import Inquiry, CategoryModel


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['category', 'date', 'first_name', 'last_name', 'phone', 'email']
    list_filter = ['category', 'date']
    search_fields = ['category', 'first_name', 'last_name']
    fieldsets = (
        ('Personal information', {
            'fields': (
                'first_name',
                'last_name',
                'town',
                'email',
                'phone',
            )}),
        ('Inquiry information', {
            'fields': (
                'category',
                'text',
            )}),
    )


admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(CategoryModel)
