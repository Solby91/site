from django.shortcuts import render, get_object_or_404
from .models import *


def GoodsList(request, category_slug=None):
    category = None
    categories = Catalog.objects.all()
    goods = Goods.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Catalog, slug=category_slug)
        goods = goods.filter(category=category)
    return render(request, 'catalog/category.html',
                              {'category': category,
                               'categories': categories,
                               'goods': goods,
                               })


def GoodPage(request, id, slug):
    good = get_object_or_404(Goods, id=id, slug=slug, available=True)
    return render(request, 'catalog/goods.html', {'good': good})