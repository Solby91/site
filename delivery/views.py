from django.shortcuts import render
from .models import Delivery


def show_delivery(request):
    info = Delivery.objects.all()
    return render(request, 'info/info.html', {
            'info': info,
    })