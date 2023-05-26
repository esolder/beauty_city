from django.shortcuts import render
from booking.models import Service, Employee, Review


def render_index(request):
    services = Service.objects.all()
    employees = Employee.objects.all()
    reviews = Review.objects.all()
    return render(request, 'index.html', {'services': services, 'employees': employees, 'reviews': reviews})


