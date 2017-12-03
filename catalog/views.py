from django.shortcuts import render, get_object_or_404
from .models import *


def category_list(request, category_slug=None):
    category = None
    categories = Catalog.objects.all()
    goods = Goods.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Catalog, slug=category_slug)
        goods = goods.filter(category=category)
    return render(request, 'catalog/category.html', {
            'category': category,
            'categories': categories,
            'goods': goods,
    })


def good_page(request, category_slug=None, slug=None):
    good = None
    category = None
    goods = Goods.objects.all()
    categories = Catalog.objects.all()
    if category_slug:
        category = get_object_or_404(Catalog, slug=category_slug)
        goods = goods.filter(category=category)
    if slug:
        good = get_object_or_404(Goods, slug=slug)
        goods = goods.filter(category=category)
    return render(request, 'catalog/goods.html', {
            'good': good,
            'category': category,
            'goods': goods,
            'categories': categories,
    })

