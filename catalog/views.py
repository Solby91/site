from django.shortcuts import render, get_object_or_404, render_to_response
from .models import *


def show_catalog(request):
    return render(request, "catalog/catalog.html",
                              {"nodes": Catalog.objects.all()},
                  )


def goods_slug(request, slug):
    goods = get_object_or_404(Goods, slug=slug)
    return render(request, 'catalog/goods.html',
                              {'goods': goods,}
                 )