from django.shortcuts import render
from .models import About


def show_about(request):
    info = About.objects.all()
    app_url = request.path
    return render(request, 'info/info.html', {
            'info': info,
            'app_url': app_url,
    })