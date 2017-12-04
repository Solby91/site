from django.contrib import admin
from .models import Catalog, Products


class ProductsAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name', )}
    search_fields = ['name']
    list_filter = ['category']
    list_display = ('name','price', 'available','category', 'vendor_code', 'slug', )
    list_editable = ['price', 'available']


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Products, ProductsAdmin)
admin.site.register(Catalog, CatalogAdmin)
