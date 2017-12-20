from django.shortcuts import render
from .models import About


def show_about(request):
    info = About.objects.all()
    return render(request, 'info/info.html', {
            'info': info,
    })