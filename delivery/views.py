from django.shortcuts import render
from .models import Delivery


def show_delivery(request):
    info = Delivery.objects.all()
    app_url = request.path
    return render(request, 'info/info.html', {
            'info': info,
            'app_url':app_url,
    })