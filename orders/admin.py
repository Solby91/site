from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
import csv
import datetime
from django.core.urlresolvers import reverse
from django.utils.html import format_html


def order_detail(obj):
    return format_html('<a href="{}">Посмотреть</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
    ))


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename=Orders-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Первая строка- оглавления
    writer.writerow([field.verbose_name for field in fields])
    # Заполняем информацией
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
    ExportToCSV.short_description = 'Export CSV'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


def order_pdf(obj):
    return format_html('<a href="{}">PDF</a>'.format(
        reverse('orders:AdminOrderPDF', args=[obj.id])
    ))


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'mobile_number', 'email', 'city',
                    'address', 'postal_code', 'paid', 'created', 'updated', order_detail,
                    order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


order_pdf.short_description = 'В PDF'
admin.site.register(Order, OrderAdmin)