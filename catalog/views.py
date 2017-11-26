from django.shortcuts import render, get_object_or_404
from .models import *


def main_page(request):
    #catalog = get_object_or_404(Catalog, slug=slug)
    nodes = Catalog.objects.all()
    return render(request, 'catalog/catalog.html',
                  {'nodes': nodes,
                   #'catalog':catalog
                   })

def show_catalog(request, slug):
    catalog = get_object_or_404(Catalog, slug=slug)
    nodes = Catalog.objects.get()
    return render(request, "catalog/category.html",
                              {"nodes": nodes,
                               "catalog": catalog,
                               })

def GoodsList(request, slug):
    goods = get_object_or_404(Goods, slug=slug)
    goods_all = Goods.objects.all()
    return render(request, 'catalog/goods.html',
                              {'goods_all': goods_all,
                               'goods': goods,
                               })
