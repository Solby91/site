from django.shortcuts import render, get_object_or_404
from .models import *


def main_page(request):
    nodes = Catalog.objects.all()
    return render(request, 'catalog/catalog.html',
                  {'nodes': nodes,
                   })


def show_catalog(request, category_slug):
    catalog = get_object_or_404(Catalog, category_slug=category_slug)
    nodes = Catalog.objects.all()
    categories = []
    for x in nodes:
        if x.parent_id == catalog.id:
            categories.append(x.name)
    return render(request, "catalog/category.html",
                              {"nodes": nodes,
                               "catalog": catalog,
                               "categories": categories,
                               })


def GoodsList(request, slug):
    goods = get_object_or_404(Goods, slug=slug)
    goods_all = Goods.objects.all()
    return render(request, 'catalog/goods.html',
                              {'goods_all': goods_all,
                               'goods': goods,
                               })
