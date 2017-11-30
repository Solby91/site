from django.contrib import admin
from .models import Catalog, Goods


class GoodsAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name', )}
    search_fields = ['name']
    list_filter = ['category']
    list_display = ('name','price', 'available','category', 'vendor_code', 'slug', )
    list_editable = ['price', 'available']


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ['tree_id']


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Catalog, CatalogAdmin)
