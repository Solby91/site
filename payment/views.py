from django.shortcuts import render
from .models import Payment


def show_payment(request):
    payment = Payment.objects.all()
    return render(request, 'payment/payment.html', {
            'payment': payment,
    })