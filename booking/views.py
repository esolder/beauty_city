from datetime import datetime
from django.core.cache import cache
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.urls import reverse
from .models import Review, Category, Employee, Appointment, Service
from .serializers import AppointmentSerializer, ReviewSerializer


class AppointmentView(TemplateView):
    template_name = 'service.html'

    def get(self, request):
        categories = Category.objects.all()
        employees = Employee.objects.all()
        context = {
            'categories': categories,
            'employees': employees,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        service = request.POST.get('service')
        employee = request.POST.get('employee')
        date = request.POST.get('date')
        time = request.POST.get('time')
        cache.set('service_id', service)
        cache.set('employee_id', employee)
        cache.set('date', date)
        cache.set('time', time)
        return redirect('serviceFinally')


class ServiceFinallyView(TemplateView):
    template_name = 'serviceFinally.html'

    def get(self, request):
        context = {
            'service': get_object_or_404(Service, pk=cache.get('service_id')),
            'employee': get_object_or_404(Employee, pk=cache.get('employee_id')),
            'date': cache.get('date'),
            'time': cache.get('time'),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        date = datetime.strptime(cache.get('date'), '%d.%m.%Y').date()

        data = {
            'service': cache.get('service_id'),
            'employee': cache.get('employee_id'),
            'date': date.isoformat(),
            'time': cache.get('time'),
            'name': request.POST.get('name'),
            'phonenumber': request.POST.get('phonenumber'),
            'comment': request.POST.get('comment'),
        }

        serializer = AppointmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return render(request, self.template_name)
        else:
            return JsonResponse({'errors': serializer.errors}, status=400)


@api_view(['POST'])
def submit_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class SubmitReview(TemplateView):
    template_name = 'reviews.html'

    def get(self, request):
        return render(request, self.template_name)


@api_view(['POST'])
def submit_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponseRedirect(reverse('reviews'))
    return Response(serializer.errors, status=400)


class TipsView(TemplateView):
    template_name = 'tips.html'

    def get(self, request):
        return render(request, self.template_name)


def get_time(request):
    employee_id = request.GET.get('employeeId')
    date = request.GET.get('date')
    formated_time_slots = []
    if employee_id and date:
        date = datetime.strptime(date, '%d.%m.%Y')
        employee = get_object_or_404(Employee, pk=employee_id)
        available_time_slots = employee.get_available_time(date)
        formated_time_slots = []
        for time_slot in available_time_slots:
            if time_slot > datetime.now().time() or date > datetime.now():
                formated_time_slots.append(time_slot.strftime('%H:%M'))  
    return JsonResponse({'available_time_slots': formated_time_slots})
