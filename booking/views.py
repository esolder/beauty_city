from datetime import datetime
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import Review, Category, Employee, Appointment, Service


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
        service = get_object_or_404(Service, pk=cache.get('service_id'))
        employee = get_object_or_404(Employee, pk=cache.get('employee_id'))
        date = datetime.strptime(cache.get('date'), '%d.%m.%Y')
        time = cache.get('time')
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        comment = request.POST.get('comment')

        appointment = Appointment(
            service=service,
            employee=employee,
            date=date,
            time=time,
            name=name,
            phonenumber=phonenumber,
            comment=comment,
        )
        appointment.save()

        return render(request, self.template_name)


class SubmitReview(TemplateView):
    template_name = 'reviews.html'

    def post(self, request):
        name = request.POST.get('name')
        employee = request.POST.get('employee')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review')

        review = Review.objects.create(
            name=name,
            employee=employee,
            rating=rating,
            text=review_text
        )

        review.save()

        message = 'Спасибо за оставленный отзыв!'
        return render(request, self.template_name, {'message': message})


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
