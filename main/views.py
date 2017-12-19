from django.shortcuts import render
from .models import Main


def show_main(request):
    main = Main.objects.all()
    return render(request, 'main/main.html', {
            'main': main,
    })