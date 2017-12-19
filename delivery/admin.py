from django.contrib import admin
from .models import Delivery


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Delivery,DeliveryAdmin)