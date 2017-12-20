from django.shortcuts import render
from .models import Contacts


def show_contacts(request):
    info = Contacts.objects.all()
    return render(request, 'info/info.html', {
            'info': info,
    })