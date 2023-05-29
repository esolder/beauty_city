import re

from datetime import datetime
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import Category, Employee, Service, Appointment, Review


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

        service = get_object_or_404(Service, pk=cache.get('service_id'))
        employee = get_object_or_404(Employee, pk=cache.get('employee_id'))

        data = {
            'service': service,
            'employee': employee,
            'date': date.isoformat(),
            'time': cache.get('time'),
            'name': request.POST.get('name'),
            'phonenumber': request.POST.get('phonenumber'),
            'comment': request.POST.get('comment'),
        }


        if not re.match(r'^\+7\d{10}$', data['phonenumber']):
            return JsonResponse({'errors': 'Номер телефона должен быть в формате: "+7xxxxxxxxxx"'}, status=400)

        try:
            appointment = Appointment.objects.create(**data)
            appointment.full_clean()
        except ValidationError as e:
            return JsonResponse({'errors': str(e)}, status=400)

        cache.set('name', data['name'])
        cache.set('date', data['date'])
        cache.set('time', data['time'])

        return redirect('serviceSuccess')


@csrf_exempt
def submit_appointment(request):
    if request.method == 'POST':
        data = request.POST

        if not re.match(r'^[а-яА-Я\s]*$', data['name']):
            return JsonResponse({'errors': 'Имя может содержать только буквы и пробелы'}, status=400)

        if not re.match(r'^\+7\d{10}$', data['phonenumber']):
            return JsonResponse({'errors': 'Номер телефона должен быть в формате: "+7xxxxxxxxxx"'}, status=400)

        service = get_object_or_404(Service, pk=data.get('service'))
        employee = get_object_or_404(Employee, pk=data.get('employee'))

        data['service'] = service
        data['employee'] = employee

        try:
            appointment = Appointment.objects.create(**data)
            appointment.full_clean()
        except ValidationError as e:
            return JsonResponse({'errors': str(e)}, status=400)

        return JsonResponse(appointment, status=201)
    else:
        return JsonResponse({'errors': 'Некорректный запрос'}, status=400)


class SubmitReview(TemplateView):
    template_name = 'reviews.html'

    def post(self, request):
        name = request.POST.get('name')
        employee = request.POST.get('employee')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review')

        Review.objects.create(
            name=name,
            employee=employee,
            rating=rating,
            text=review_text
        )

        message = 'Спасибо за оставленный отзыв!'
        return render(request, self.template_name, {'message': message})


class TipsView(TemplateView):
    template_name = 'tips.html'

    def get(self, request):
        return render(request, self.template_name)


class ServiceSuccessView(TemplateView):
    template_name = 'servicesuccess.html'

    def get(self, request):
        context = {
            'name': cache.get('name'),
            'date': cache.get('date'),
            'time': cache.get('time'),
        }
        cache.delete('name')
        cache.delete('date')
        cache.delete('time')
        return render(request, self.template_name, context)


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
