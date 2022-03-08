from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.contrib import admin
from django.utils.html import format_html
from django.db import transaction
from .models import Order


def refund(modeladmin, request, queryset):
    with transaction.atomic():
        qs = queryset.filter(~Q(status='refund'))

        ct = ContentType.objects.get_for_model(queryset.model)
        for obj in qs:
            obj.product.stock += obj.quantity
            obj.product.save()
        qs.update(status='refund')

        LogEntry.objects.log_action(
            user_id=request.user.id,
            content_type_id=ct.pk,
            object_id=obj.pk,
            object_repr='Refund Order',
            action_flag=CHANGE,
            change_message='Refund Order',
        )

refund.short_description = 'Refund'


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('user', 'product', 'styled_status')

    actions = [
        refund
    ]
    
    def styled_status(self, obj):
        if obj.status == 'refund':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        if obj.status == 'confirmed':
            return format_html(f'<span style="color:green">{obj.status}</span>')
        return obj.status

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': 'Order List' }
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        order = Order.objects.get(pk=object_id)
        extra_context = {'title': f'Change {order.product.name} of {order.user.email}'}
        return super().changeform_view(request, object_id, form_url, extra_context)

    styled_status.short_description = 'Status'

admin.site.register(Order, OrderAdmin)
