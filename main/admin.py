from django.contrib import admin
from .models import Main


class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Main,MainAdmin)