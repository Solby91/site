from django.shortcuts import render, get_object_or_404, render_to_response
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
    })


def product_page(request, category_slug, slug):
    products = Products.objects.all()
    category = get_object_or_404(Catalog, slug=category_slug)
    product = get_object_or_404(Products,  slug=slug)
    products = products.filter(category=category)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/products.html', {
            'product': product,
            'category': category,
            'products': products,
            'cart_product_form': cart_product_form
          })

