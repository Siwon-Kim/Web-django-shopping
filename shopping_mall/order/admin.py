from django.contrib import admin
from django.utils.html import format_html
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('user', 'product', 'styled_status')

    def styled_status(self, obj):
        if obj.status == 'refund':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        if obj.status == 'confirmed':
            return format_html(f'<span style="color:green">{obj.status}</span>')
        return obj.status

    styled_status.short_description = 'Status'

admin.site.register(Order, OrderAdmin)
