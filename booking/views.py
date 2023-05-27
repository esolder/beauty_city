from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Review, Category, Employee


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


class ServiceFinallyView(TemplateView):
    template_name = 'serviceFinally.html'

    def get(self, request):
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


def get_time(request):
    employee_id = request.GET.get('employee_id')
    date = request.GET.get('date')
    date = datetime.strptime(date, '%d.%m.%Y')
    employee = Employee.objects.filter(pk=employee_id)
    available_time_slots = employee.appointments.filter(date=date)
    return [time_slot.strftime('%H:%M') for time_slot in available_time_slots]
