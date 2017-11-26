from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Catalog, Goods


class GoodsAdmin(admin.ModelAdmin):
    fields = ['name','price', 'parent', 'description','vendor_code', 'slug', ]
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ['name']
    list_filter = ['parent']


class CatalogAdmin(admin.ModelAdmin):
    fields = ['name', 'parent', 'slug', ]
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ['parent', 'tree_id']

admin.site.register(Goods, GoodsAdmin)
admin.site.register(Catalog, CatalogAdmin)
