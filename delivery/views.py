from django.shortcuts import render
from .models import Delivery


def show_delivery(request):
    delivery = Delivery.objects.all()
    return render(request, 'delivery/delivery.html', {
            'delivery': delivery,
    })