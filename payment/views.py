from django.shortcuts import render
from .models import Payment


def show_payment(request):
    info = Payment.objects.all()
    app_url = request.path
    return render(request, 'info/info.html', {
        'info': info,
        'app_url': app_url,
    })