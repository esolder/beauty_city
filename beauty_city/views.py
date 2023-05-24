from django.shortcuts import render
from booking.models import Service


def render_index(request):
    return render(request, 'index.html')


def my_view(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'objects': services})