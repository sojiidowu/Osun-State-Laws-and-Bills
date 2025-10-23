from django.contrib import admin
from .models import Category, BillOrLaw, Payment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']


@admin.register(BillOrLaw)
class BillOrLawAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'category',
                    'price', 'is_free')
    list_filter = ['type', 'category', 'is_free']
    search_fields = ['title', 'description']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'bill_or_law', 'amount',
                    'status', 'reference')
    list_filter = ['status']
    search_fields = ['reference', 'user__username']
