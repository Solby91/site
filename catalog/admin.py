from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Catalog, Goods


class GoodsAdmin(admin.ModelAdmin):
    fields = ['name','price', 'parent', 'description','vendor_code', 'slug']
    search_fields = ['name']
    list_filter = ['parent']



admin.site.register(Goods, GoodsAdmin)

admin.site.register(
    Catalog,
    DraggableMPTTAdmin,
    list_display = (
        'tree_actions',
        'indented_title',
        ),
    list_display_links = (
        'tree_actions',
        ),
    mptt_level_indent = 30
    )