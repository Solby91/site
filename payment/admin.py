from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Payment,PaymentAdmin)