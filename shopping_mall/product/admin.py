from django.contrib import admin
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_format', 'styled_stock')

    def price_format(self, obj):
        price = intcomma(obj.price)
        return f'$ {price}'

    def styled_stock(self, obj):
        stock = intcomma(obj.stock)
        if obj.stock <= 50:
            return format_html(f'<b><span style="color:red">{stock}</span></b>')
        return stock

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': 'Product List' }
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        product = Product.objects.get(pk=object_id)
        extra_context = {'title': f'Change {product.name}'}
        return super().changeform_view(request, object_id, form_url, extra_context)

    price_format.short_description = 'price'
    styled_stock.short_description = 'stock'

admin.site.register(Product, ProductAdmin)
