from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm


def category_list(request, category_slug=None):
    category = None
    categories = Catalog.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Catalog, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'catalog/category.html', {
            'category': category,
            'categories': categories,
            'products': products,
            'category_slug': category_slug,
    })


def product_page(request, category_slug, slug):
    products = Products.objects.all()
    category = get_object_or_404(Catalog, slug=category_slug)
    categories = Catalog.objects.all()
    product = get_object_or_404(Products,  slug=slug)
    products = products.filter(category=category)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/products.html', {
            'product': product,
            'category': category,
            'products': products,
            'cart_product_form': cart_product_form,
            'categories': categories,
          })


def search_view (request):
    products = Products.objects.all()
    product = get_object_or_404(Products)
    return render(request, 'catalog/base.html', {
        'product': product,
        'products': products,
    })