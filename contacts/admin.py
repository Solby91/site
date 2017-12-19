from django.contrib import admin
from .models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Contacts,ContactsAdmin)