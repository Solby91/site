from django.shortcuts import render
from .models import Contacts


def show_contacts(request):
    info = Contacts.objects.all()
    app_url = request.path
    return render(request, 'info/info.html', {
            'info': info,
            'app_url':app_url,
    })