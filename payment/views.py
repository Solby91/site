from django.shortcuts import render
from .models import Payment


def show_payment(request):
    info = Payment.objects.all()
    return render(request, 'info/info.html', {
            'info': info,
    })