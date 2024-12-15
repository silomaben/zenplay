from django.contrib import admin
from .models import Accessory

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock_quantity', 'price', 'date_added')
    search_fields = ('name', 'category')
    list_filter = ('category',)
