from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Review


class AppointmentView(TemplateView):
    template_name = 'service.html'

    def get(self, request):
        return render(request, self.template_name)


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









