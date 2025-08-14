from django.contrib import admin
from storage.models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('phone', 'color', 'memory_size', 'frame', 'quantity')
    list_filter = ('phone', 'color', 'memory_size', 'frame')
    search_fields = ('phone__model',)
    raw_id_fields = ('phone', 'color', 'memory_size', 'frame')

