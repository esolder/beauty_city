from django.shortcuts import render
from booking.models import Service, Employee


def render_index(request):
    services = Service.objects.all()
    employees = Employee.objects.all()
    return render(request, 'index.html', {'services': services, 'employees': employees})


