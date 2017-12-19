from django.shortcuts import render
from .models import About


def show_about(request):
    abouts = About.objects.all()
    return render(request, 'about/about.html', {
            'abouts': abouts,
    })